#!/usr/bin/env python3
"""
This module provides a function to create an asyncio Task for a given delay.

Functions:
    task_wait_random(max_delay: int) -> asyncio.Task:
        Creates an asyncio Task that waits for a random delay.

Example usage:
    task = task_wait_random(5)
"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio Task that waits for a random delay.
    Args:
        max_delay (int): The maximum delay in seconds.
    Returns:
        asyncio.Task: An asyncio Task that will complete after a random delay.
    """
    return asyncio.create_task(wait_random(max_delay))