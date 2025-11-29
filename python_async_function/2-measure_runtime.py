#!/usr/bin/env python3
"""
Function that measures the average runtime of the wait_n coroutine
using time-based benchmarking.
"""
import asyncio
import time
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Args:
        n (int): Number of coroutines to run.
        max_delay (int): Maximum delay for each coroutine.

    Returns:
        float: Average execution time per coroutine.
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    total_time = end_time - start_time
    return total_time / n
