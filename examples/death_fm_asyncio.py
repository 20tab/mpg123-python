from mpg123 import Mpg123, Out123
import asyncio
import aiohttp

mp3 = Mpg123()

out = Out123()

async def radio_streaming(mp3, out):
    async with aiohttp.ClientSession() as session:
        async with session.get('http://hi5.death.fm') as response:
            while True:
                chunk = await response.content.read(4096)
                if not chunk:
                    break
                mp3.feed(chunk)
                for frame in mp3.iter_frames(out.start):
                    out.play(frame)

loop = asyncio.get_event_loop()
loop.run_until_complete(radio_streaming(mp3, out))
