from mpg123 import Mpg123, Out123
import asyncio

"""
This is a really special test as we check if the mp3 parser is robust
enough to survive a blind-tcp session instead of http full parsing
"""

mp3 = Mpg123()

out = Out123()

async def radio_streaming(mp3, out):
    reader, writer = await asyncio.open_connection('hi5.death.fm', 80)
    writer.write('GET / HTTP/1.0\r\n\r\n'.encode())

    while True:
        chunk = await reader.read(4096)
        if not chunk:
            break
        mp3.feed(chunk)
        for frame in mp3.iter_frames(out.start):
            out.play(frame)

loop = asyncio.get_event_loop()
loop.run_until_complete(radio_streaming(mp3, out))
