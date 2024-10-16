#!/usr/bin/env python3
"""Run time for four parallel comprehensions using asynio.gather"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the runtime of four parallel coroutine
    functions with asyncio.gather - 10sec
    """
    start_time = time.perf_counter()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    elapsed_time = time.perf_counter() - start_time

    return elapsed_time
