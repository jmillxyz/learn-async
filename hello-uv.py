import asyncio
import uvloop
from aiohttp import ClientSession

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

async def hello():
    async with ClientSession() as session:
        async with session.get("http://httpbin.org/headers") as response:
            response = await response.read()
            print(response)

loop = asyncio.get_event_loop()

loop.run_until_complete(hello())

