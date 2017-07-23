# mpg123-python
mpg123 python wrapper using ctypes

CPython 2 and 3 are supported as well as PyPy

## Quick intro

this is a simple mp3 player (libout123 is part of the mpg123 distribution)

```python
from mpg123 import Mpg123, Out123

# load an mp3 file
mp3 = Mpg123('tests/bensound-scifi.mp3')

# use libout123 to access the sound device
out = Out123()

# decode mp3 frames and send them to the sound device
for frame in mp3.iter_frames(out.start):
    out.play(frame)
```

## Test suite

The example files are "Royalty Free Music from Bensound" (http://www.bensound.com). For all of the test files a ID3v1 record has been aded
