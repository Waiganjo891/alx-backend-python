#!/usr/bin/env python3
"""
Module to measure the runtime of executing async_comprehension
function four times in parallel using asyncio.gather.
"""
import asyncio
import time
from typing import List


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using an async
    comprehension over async_generator.
    Returns:
        List of 10 random float numbers.
    """
    import random

    async def async_generator():
        """
        Coroutine that yields a random float between 0 and 10,
        10 times, one at a time with a 1-second delay in between.
        """
        for _ in range(10):
            await asyncio.sleep(1)
            yield random.uniform(0, 10)

    return [number async for number in async_generator()]


async def measure_runtime() -> float:
    """
    Coroutine that measures the total runtime of executing
    async_comprehension function four times in parallel.
    Returns:
        Total runtime in seconds.
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time


if __name__ == "__main__":
    import asyncio

    async def main():
        total_runtime = await measure_runtime()
        print(total_runtime)
    asyncio.run(main())
