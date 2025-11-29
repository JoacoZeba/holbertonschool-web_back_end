#!/usr/bin/env python3
"""
function to create an asyncio Task that runs the wait_random 
coroutine from the '0-basic_async_syntax' module.
"""
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """
    Args:
        max_delay (int): Maximum delay for wait_random.

    Returns:
        asyncio.Task: The scheduled asyncio Task.
    """
    return asyncio.create_task(wait_random(max_delay))
