import asyncio
import random

async def function(number):
    await asyncio.sleep(random.uniform(0.1, 0.5))
    return number * 2

async def main():
    numbers = [1, 2, 3, 4, 5]
    tasks = [function(num) for num in numbers]
    result = await asyncio.gather(*tasks)
    print (result)

asyncio.run(main())



