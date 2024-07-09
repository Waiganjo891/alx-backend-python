#!/usr/bin/env python3
"""
This module contains a function to measure
the average runtime of wait_n.
"""
import time
from typing import Union
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns the average time per task.
    Args:
        n (int): Number of tasks to run.
        max_delay (int): Maximum delay for each task.
    Returns:
        float: Average time per task.
    """
    start_time = time.time()
    wait_n(n, max_delay)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n


if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
