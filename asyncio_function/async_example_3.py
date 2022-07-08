import asyncio

async def call():
    print("hello")

async def main():
    first= asyncio.create_task(call())
    await first

asyncio.run(main())
    