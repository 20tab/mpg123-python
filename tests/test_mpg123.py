import unittest
from mpg123 import Mpg123


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

    def test_file_format(self):
        mp3 = Mpg123('tests/bensound-epic.mp3')
        rate, channels, width = mp3.get_format()
        self.assertEqual(rate, 44100)
        self.assertEqual(channels, 2)
        self.assertEqual(width, 2)

    def test_file_frame(self):
        mp3 = Mpg123('tests/bensound-epic.mp3')
        frame = mp3.decode_frame()
        self.assertEqual(len(frame), 188)
        frame = mp3.decode_frame()
        self.assertEqual(len(frame), 4608)

    def test_file_all_frames(self):
        mp3 = Mpg123('tests/bensound-epic.mp3')
        frames = [frame for frame in mp3.iter_frames()]
        self.assertEqual(len(frames), 6835)

if __name__ == '__main__':
    unittest.main()
