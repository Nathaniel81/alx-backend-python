#!/usr/bin/env python3
"""
Provides a coroutine that waits for a random delay between 0
and a specified time, and then returns that delay
"""
import random
import asyncio


async def wait_random(max_delay=10):
    """
    Wait for a random delay between 0 and `max_delay` seconds (inclusive),
    and then return the delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
