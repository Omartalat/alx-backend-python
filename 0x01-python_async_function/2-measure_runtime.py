#!/usr/bin/env python3
"""
task 2
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average runtime of executing wait_n function.
    Args:
        n (int): The number of times to execute wait_n.
        max_delay (int): The maximum delay for each wait_n call.
    Returns:
        float: The average runtime per execution of wait_n.
    """

    start_time: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time: float = time.time()
    return (end_time - start_time) / n
