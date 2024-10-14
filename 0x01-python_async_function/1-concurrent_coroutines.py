#!/usr/bin/env python3
"""
This module contains an asynchronous function that executes multiple coroutines
concurrently.

Functions:
    wait_n(n: int, max_delay: int) -> List[float]:
        Executes the wait_random coroutine n times with
        a maximum delay of max_delay.
        Returns a list of the delays (float) in the order they were executed.
"""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute multiple coroutines concurrently and return their results.
    Args:
        n (int): The number of coroutines to execute.
        max_delay (int): The maximum delay for each coroutine.
    Returns:
        List[float]: A list of delays in seconds for each coroutine.
    """

    _list: List[float] = []

    for _ in range(n):
        _list.append(await wait_random(max_delay))
    return sorted(_list)
