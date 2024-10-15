#!/usr/bin/env python3
'''hello world what are you doing here
'''
import time
import random
import asyncio


async def wait_random(max_delay=10):
    '''why are you asking
    '''
    r = random.uniform(0, max_delay)
    await asyncio.sleep(r)
    return r
