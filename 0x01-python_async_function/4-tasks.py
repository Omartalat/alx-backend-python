#!/usr/bin/env python3
"""
This module contains an asynchronous function that waits for a random delay.

Functions:
    task_wait_n(n: int, max_delay: int) -> List[float]:
        Spawns `n` tasks that wait for a random delay up to `max_delay`
        seconds and returns a list of the delays in ascending order.
"""
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    _list: List[float] = []

    for _ in range(n):
        _list.append(await task_wait_random(max_delay))
    return sorted(_list)
