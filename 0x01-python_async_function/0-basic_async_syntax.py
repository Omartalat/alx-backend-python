#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine that waits for a random delay.

Functions:
    wait_random(max_delay: int = 10) -> float:
        Asynchronous coroutine that waits for a random delay between 0 and
        max_delay seconds.
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous function that waits for a random delay between 0
    and max_delay seconds.
    Args:
        max_delay (int): The maximum number of seconds to wait. Default is 10.
    Returns:
        delay (float): The actual number of seconds waited.
    """

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
