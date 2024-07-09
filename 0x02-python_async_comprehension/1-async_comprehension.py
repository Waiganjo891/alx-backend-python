#!/usr/bin/env python3
"""
Module to collect random numbers using an asynchronous generator.
"""
from typing import List
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine to collect 10 random numbers using async
    comprehension over async_generator.
    Returns:
        List[float]: A list containing 10 random floating-point
        numbers.
    """
    return [i async for i in async_generator()][:10]
