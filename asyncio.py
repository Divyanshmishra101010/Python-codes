import time
import asyncio

async def func1():
    time.sleep(3)
    print('func1')
    return 1

async def func2():
    time.sleep(3)
    print('func2')
    return 2

async def func3():
    time.sleep(3)
    print('func3')
    return 3

async def main():
    result = await asyncio.gather(
        func1(),
        func2(),
        func3(),
    )
    return result

result = asyncio.run(main())
    