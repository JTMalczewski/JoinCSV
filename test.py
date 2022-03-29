import unittest
from tools import read, join_fun, draw
import numpy as np

class TestCSV(unittest.TestCase):

    def test_quotation_marks (self):
        self.assertEqual(
            read.splitRow(
                ["Index,\"Height\",Weight\n",
                "1, 65.78, 112.99\n"]),

                [["Index", "\"Height\"", "Weight"],
                ["1", " 65.78", " 112.99"]],

                "spliting rows with \"[word]\" don't work")

    def test_no_line_break(self):
        self.assertEqual(
            read.splitRow(
                ["Index,Height,Weight\n",
                "1, 65.78, 112.99"]),

                [["Index", "Height", "Weight"],
                ["1", " 65.78", " 112.99"]],

                "spliting rows with no break symbol don't work")

    def test_comma_in_quotes(self):
        self.assertEqual(
            read.splitRow(
                ["Index,\"Hei,ght\",Weight\n",
                "1, 65.78, 112.99"]),

                [["Index", "\"Hei,ght\"", "Weight"],
                ["1", " 65.78", " 112.99"]],

                "spliting rows with \",\" don't work")

if __name__ == '__main__':
    unittest.main()