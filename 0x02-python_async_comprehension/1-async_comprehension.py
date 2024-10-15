#!/usr/bin/env python3
"""
Asynchronously collects 10 random numbers using an async comprehending over
async_generator and returns them.

Returns:
    List[float]: A list of 10 random floating-point numbers.
"""
from typing import AsyncGenerator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> AsyncGenerator[float, None]:
    """
    Asynchronously collects 10 random numbers using an async comprehending over
    a generator.
    Returns:
        List[float]: A list of 10 random floating-point numbers.
    """

    nums = [i async for i in async_generator()]
    return nums
