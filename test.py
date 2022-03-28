import unittest
from package import read

class TestCSV(unittest.TestCase):

    def test_clear(self):
        self.assertEqual(1,1,"test file isn't working")

if __name__ == '__main__':
    unittest.main()