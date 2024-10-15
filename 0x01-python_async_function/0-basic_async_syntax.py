#!/usr/bin/env python3
"""The basics of async"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that takes in an integer argument
    and returns a float from 0 to max_delay (included) seconds.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
