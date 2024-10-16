#!/usr/bin/env python3
"""Async Comprehensions"""
import asyncio
from typing import List
import random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    A coroutine that collects 10 random numbers from async_generator
    using an async comprehension and returns them.
    """
    result = [i async for i in async_generator()]

    return result
