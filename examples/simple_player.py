from mpg123 import Mpg123, Out123

mp3 = Mpg123('tests/bensound-scifi.mp3')

out = Out123()

for frame in mp3.iter_frames(out.start):
    out.play(frame)
