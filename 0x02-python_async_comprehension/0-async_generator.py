#!/usr/bin/env python3
"""
This module contains an asynchronous generator function.

Functions:
    async_generator: Asynchronously yields random floating-point numbers between 0 and 10.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    An asynchronous generator that yields random floating-point numbers.
    This coroutine will asynchronously yield a random float between 0 and 10,
    one at a time, with a 1-second delay between each yield.
    Yields:
        float: A random floating-point number between 0 and 10.
    """

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
