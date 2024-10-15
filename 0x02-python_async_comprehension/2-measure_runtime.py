#!/usr/bin/env python3
"""
This module measures the runtime of executing
the async_comprehension function four times in parallel.

Functions:
    measure_runtime: Asynchronously executes async_comprehension
    four times in parallel and measures the total runtime.

Usage:
    This script is intended to be run as a standalone module or
    imported into another module.
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """
    Measures the total runtime of executing the `async_comprehension`
    function four times concurrently.
    This function uses `asyncio.gather` to run four instances of
    `async_comprehension` concurrently
    and measures the time taken to complete all of them.
    Returns:
        float: The total runtime in seconds.
    """
    start = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end = time.time()
    return end - start
