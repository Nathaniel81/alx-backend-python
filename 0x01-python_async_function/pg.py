from typing import List
import asyncio
import random
import time
# wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and `max_delay` seconds (inclusive),
    and then return the delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times with the specified max_delay"""
    tasks = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)
    results = []
    for completed_task in asyncio.as_completed(tasks):
        result = await completed_task
        results.append(result)
    return results
# wait_n = __import__('1-concurrent_coroutines').wait_n

# print(asyncio.run(wait_n(5, 5)))
# print(asyncio.run(wait_n(10, 7)))
# print(asyncio.run(wait_n(10, 0)))

def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay), and return
    the average time per task in seconds.
    """
    start_time = time.time()  # Record start time
    asyncio.run(wait_n(n, max_delay))  # Run wait_n in an event loop
    end_time = time.time()  # Record end time
    total_time = end_time - start_time  # Calculate total time
    avg_time = total_time / n  # Calculate average time per task
    return avg_time
def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio.Task for the wait_random coroutine with the specified max_delay
    """
    return asyncio.create_task(wait_random(max_delay))

# async def test(max_delay: int) -> float:
#     task = task_wait_random(max_delay)
#     await task
#     print(task.__class__)

# asyncio.run(test(5))
