#!/usr/bin/env python3
"""Measure the runtime of a coroutine function"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measure_time: function that measures the total execution time for wait_n
    params: n: int (number of tasks)
    params: max_delay: int (maximum delay for each task)
    return: average time per task: float
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - start_time
    return elapsed / n
