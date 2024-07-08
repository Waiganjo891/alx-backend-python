#!/usr/bin/env python3
"""
This module provides an async routine called wait_n that spawns
wait_random n times with the specified max_delay and returns the
list of delays in ascending order.
"""
import asyncio
from typing import List
from random import uniform


async def wait_random(max_delay: int) -> float:
    """
    Asynchronously wait for a random delay between 0 and max_delay seconds.
    Args:
        max_delay (int): The maximum delay in seconds.
    Returns:
        float: The actual delay.
    """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay and return
    the list of delays in ascending order.
    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay for wait_random.
    Returns:
        List[float]: A list of delays in ascending order.
    """
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)


if __name__ == "__main__":
    import asyncio
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
