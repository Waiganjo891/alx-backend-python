#!/usr/bin/env python3
"""
This module provides a function to create multiple asyncio
tasks that wait for random delays.
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Create multiple asyncio tasks that wait for random delays.
    Args:
        n (int): The number of tasks to create.
        max_delay (int): The maximum delay in seconds for each task.
    Returns:
        List[float]: A list of delays in seconds,
        sorted in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
