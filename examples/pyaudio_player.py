import mpg123
import pyaudio

mp3 = mpg123.Mpg123('tests/bensound-epic.mp3')

rate, channels, encoding = mp3.get_format()

p = pyaudio.PyAudio()

# conversion table between mpg123 and pyaudio
ENCODINGS_TABLE = {
    mpg123.ENC_SIGNED_8: pyaudio.paInt8,
    mpg123.ENC_SIGNED_16: pyaudio.paInt16,
    mpg123.ENC_SIGNED_24: pyaudio.paInt24,
    mpg123.ENC_SIGNED_32: pyaudio.paInt32,
    mpg123.ENC_FLOAT_32: pyaudio.paFloat32,
    mpg123.ENC_UNSIGNED_8: pyaudio.paUInt8,
}

stream = p.open(channels=channels, format=pyaudio.paInt16, rate=rate, output=True)

for frame in mp3.iter_frames():
    stream.write(frame)

p.terminate()
