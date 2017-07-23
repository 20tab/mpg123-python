import unittest
import mpg123
from mpg123 import Mpg123
import sys


class TestMpg123(unittest.TestCase):

    def test_feeding_need_more(self):
        mp3 = Mpg123()
        mp3.feed(b'')
        with self.assertRaises(Mpg123.NeedMoreException):
            mp3.decode_frame()

    def test_feeding_need_more_not_empty(self):
        mp3 = Mpg123()
        mp3.feed(b'\0\0\0\0')
        with self.assertRaises(Mpg123.NeedMoreException):
            mp3.decode_frame()

    def test_get_format_need_more(self):
        mp3 = Mpg123()
        with self.assertRaises(Mpg123.NeedMoreException):
            mp3.get_format()

    def test_feeding_need_more_bytearray(self):
        mp3 = Mpg123()
        mp3.feed(bytearray(8))
        with self.assertRaises(Mpg123.NeedMoreException):
            mp3.decode_frame()

    def test_feeding_need_more_string(self):
        mp3 = Mpg123()
        mp3.feed('hello')
        with self.assertRaises(Mpg123.NeedMoreException):
            mp3.decode_frame()

    def test_feeding_file(self):
        mp3 = Mpg123()
        with open('tests/bensound-scifi.mp3', 'rb') as f:
            while True:
                data = f.read(4096)
                if not data:
                    break
                mp3.feed(data)
        rate, channels, encoding = mp3.get_format()
        self.assertEqual(rate, 44100)
        self.assertEqual(channels, 2)
        self.assertEqual(encoding, 208)
        self.assertEqual(mp3.get_width_by_encoding(encoding), 2)
        self.assertEqual(encoding, mpg123.ENC_SIGNED_16)
        frame = mp3.decode_frame()
        self.assertEqual(len(frame), 188)
        frame = mp3.decode_frame()
        self.assertEqual(len(frame), 4608)

    def test_file_format(self):
        mp3 = Mpg123('tests/bensound-epic.mp3')
        rate, channels, encoding = mp3.get_format()
        self.assertEqual(rate, 44100)
        self.assertEqual(channels, 2)
        self.assertEqual(encoding, 208)

    def test_file_format2(self):
        mp3 = Mpg123('tests/bensound-scifi.mp3')
        rate, channels, encoding = mp3.get_format()
        self.assertEqual(rate, 44100)
        self.assertEqual(channels, 2)
        self.assertEqual(encoding, 208)

    def test_file_frame(self):
        mp3 = Mpg123('tests/bensound-epic.mp3')
        frame = mp3.decode_frame()
        self.assertEqual(len(frame), 188)
        frame = mp3.decode_frame()
        self.assertEqual(len(frame), 4608)

    def test_file_id3(self):
        mp3 = Mpg123('tests/bensound-epic.mp3')
        id3 = mp3.get_id3()
        self.assertEqual(id3.artist, 'Bensound'.encode())
        self.assertEqual(id3.year, '2017'.encode())
        self.assertEqual(id3.genre, 0)

    def test_file_id3_song2(self):
        mp3 = Mpg123('tests/bensound-scifi.mp3')
        id3 = mp3.get_id3()
        self.assertEqual(id3.artist, 'http://www.bensound.com'.encode())
        self.assertEqual(id3.year, '2012'.encode())
        self.assertEqual(id3.genre, 1)

    def test_file_all_frames(self):
        mp3 = Mpg123('tests/bensound-epic.mp3')
        frames = [frame for frame in mp3.iter_frames()]
        self.assertEqual(len(frames), 6835)

    def test_file_frame_data(self):
        mp3 = Mpg123('tests/bensound-epic.mp3')
        frames = [frame for frame in mp3.iter_frames()]
        if sys.version_info[0] >= 3:
            self.assertEqual(frames[17][22], 30)
        else:
            self.assertEqual(ord(frames[17][22]), 30)

    def test_file_length(self):
        mp3 = Mpg123('tests/bensound-epic.mp3')
        self.assertEqual(mp3.length(), 7872625)

    def test_file_frame_length(self):
        mp3 = Mpg123('tests/bensound-epic.mp3')
        self.assertEqual(mp3.frame_length(), 6835)

    def test_feed_frame_length(self):
        mp3 = Mpg123()
        with self.assertRaises(Mpg123.NeedMoreException):
            mp3.frame_length()

    def test_feed_length(self):
        mp3 = Mpg123()
        with self.assertRaises(Mpg123.NeedMoreException):
            mp3.length()

if __name__ == '__main__':
    unittest.main()
