from mpg123 import Mpg123
import wave

mp3 = Mpg123('tests/bensound-epic.mp3')
rate, channels, encoding = mp3.get_format()

wav = wave.open('bensound-epic.wav', 'wb')
wav.setnchannels(channels)
wav.setframerate(rate)
wav.setsampwidth(mp3.get_width_by_encoding(encoding))

for frame in mp3.iter_frames():
    wav.writeframes(frame)

wav.close()
