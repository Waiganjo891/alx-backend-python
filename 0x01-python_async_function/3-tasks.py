#!/usr/bin/env python3
"""
Module for asyncio task creation.
"""
import asyncio
from typing import Coroutine


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between
    0 and max_delay (inclusive) seconds and returns the delay.
    Args:
        max_delay (int): The maximum delay time in seconds.
        Default is 10.
    Returns:
        float: The actual delay time.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Regular function that creates and returns an asyncio
    Task for wait_random coroutine with the given max_delay.
    Args:
        max_delay (int): The maximum delay time in seconds.
    Returns:
        asyncio.Task: The asyncio task object.
    """
    return asyncio.create_task(wait_random(max_delay))


if __name__ == "__main__":
    async def test(max_delay: int) -> None:
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)

    asyncio.run(test(5))
