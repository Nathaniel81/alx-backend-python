#!/usr/bin/env python3
"""Doc"""


import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    '''Generates a sequence of 10 numbers.'''
    return (random.random() * 10 async for _ in asyncio.range(10))
