#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine that waits for
a random delay and returns the delay time, as well as another
coroutine that runs multiple instances of the first coroutine
and returns the delays in ascending order.
"""
import asyncio
from typing import List
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns wait_random n times
    with the specified max_delay and returns a list of all
    the delays (float values) in ascending order.
    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay time for wait_random.
    Returns:
        List[float]: A list of delay times in ascending order.
    """
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)
