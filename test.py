import unittest
from tools import read, join_fun, draw
import numpy as np

class TestCSV(unittest.TestCase):

    def test_clear(self):
        self.assertEqual(1,1,"test file isn't working")

    # def test_names(self):
    #     '''
    #     Tests possibility of write wrong column name
    #     '''
    #     self.assertEqual(read.findMatchingRows(
    #         np.array([['In','He', 'We'],
    #         ['1', '65.78', '112.99'],
    #         ['2', '71.52', '136.49']]),
    #         np.array([['Inn','Hee', 'Wee'],
    #         ['1', '65.78', '112.99'],
    #         ['2', '71.52', '136.49']]),
    #         'We'
    #     ), [[],[]],"unpredictible result, no common index")

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

                "spliting rows with no break symbol don't")

    def test_comma_in_quotes(self):
        self.assertEqual(
            read.splitRow(
                ["Index,\"Hei,ght\",Weight\n",
                "1, 65.78, 112.99"]),

                [["Index", "\"Hei,ght\"", "Weight"],
                ["1", " 65.78", " 112.99"]],

                "spliting rows with \"\" don't work")

if __name__ == '__main__':
    unittest.main()