from compressor import compress
import unittest


class CompressTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_compress_empty_string(self):
        """
        compress an empty string as an empty string
        """
        self.assertEqual(compress(""), "")

    def test_compress_single_char(self):
        """
        compress a single char string as itself
        """
        self.assertEqual(compress("a"), "a")

    def test_compress_two_different_chars(self):
        """
        compress a two different chars string as itself
        """
        self.assertEqual(compress("ab"), "ab")

    def test_compress_two_repeated_chars(self):
        """
        compress a two repeated chars string as char2
        """
        self.assertEqual(compress("aa"), "a2")

    def test_compress_some_chars_repeated_more_than_twice(self):
        """
        compress a string with some repeated chars
        """
        self.assertEqual(compress("asdfff"), "asdf3")

    def test_compress_some_chars_with_more_than_one_group(self):
        """
        compress a string with some repeated chars in more than one block
        """
        self.assertEqual(compress("aassdfffg"), "a2s2df3g")

if __name__ == '__main__':
    unittest.main()