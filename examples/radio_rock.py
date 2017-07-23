from mpg123 import Mpg123, Out123
try:
    # old python2
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen

mp3 = Mpg123()

out = Out123()

response = urlopen('http://178.32.136.160:8050')

while True:
    chunk = response.read(4096)
    if not chunk:
        break
    mp3.feed(chunk)
    for frame in mp3.iter_frames(out.start):
        out.play(frame)
