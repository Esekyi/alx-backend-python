#!/usr/bin/env python3
"""Tasks"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create an asyncio task"""
    task: asyncio.Task = asyncio.create_task(wait_random(max_delay))
    return task
