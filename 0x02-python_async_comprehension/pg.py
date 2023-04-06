import asyncio
import random
import time

async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

# asyncio.run(print_yielded_values())
async def async_comprehension():
    return [num async for num in async_generator()]

# async def main():
#     print(await async_comprehension())

# asyncio.run(main())

async def measure_runtime():
    start = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end = time.time()
    
    return end - start
    
async def main():
    return await(measure_runtime())

print(
    asyncio.run(main())
)
