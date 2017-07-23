# mpg123-python
mpg123 python wrapper using ctypes

CPython 2 and 3 are supported as well as PyPy

## Quick intro

this is a simple mp3 player using the first available sound device as the output (libout123 is part of the mpg123 distribution)

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

this is another example showing how to encode an mp3 to a wave file:

```python
from mpg123 import Mpg123
import wave

mp3 = Mpg123('tests/bensound-epic.mp3')

# get informations about the file
rate, channels, encoding = mp3.get_format()

# prepare the wave header
wav = wave.open('bensound-epic.wav', 'wb')
wav.setnchannels(channels)
wav.setframerate(rate)
wav.setsampwidth(mp3.get_width_by_encoding(encoding))

# fill the wave file
for frame in mp3.iter_frames():
    wav.writeframes(frame)

wav.close()
```

## Test suite

The example files are "Royalty Free Music from Bensound" (http://www.bensound.com). For all of the test files a ID3v1 record has been aded
