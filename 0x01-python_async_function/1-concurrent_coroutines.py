#!/usr/bin/env python3
""" Concurrent coroutines"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.
    Returns a list of delays in ascending order (without using sort()).
    """
    delays = []
    for _ in range(n):
        delays.append(await wait_random(max_delay))
    return sorted(delays)
