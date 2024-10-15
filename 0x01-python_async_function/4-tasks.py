#!/usr/bin/env python3
"""Spawn wait_random n times with the specified
max_delay and return the delays in ascending order
"""
import concurrent.futures
import asyncio
import typing
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """Spawn wait_random n times with the specified max_delay
    and return the delays in ascending order
    """
    tasks = []
    queue = []
    for _ in range(n):
        tasks.append(task_wait_random(max_delay))
    for task in asyncio.as_completed(tasks):
        result = await task
        queue.append(result)
    return queue
