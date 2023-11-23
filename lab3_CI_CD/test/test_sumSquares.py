import unittest

from sum_func import sumSquares
from fractions import Fraction

class TestSumSquares(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sumSquares(data)
        self.assertEqual(result, 14)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 2), Fraction(1, 2), Fraction(3, 4)]
        result = sumSquares(data)
        self.assertEqual(result, 1.0625)

    def test_bad_type(self):
        data = "banana"
        with self.assertRaises(TypeError):
            result = sumSquares(data)

if __name__ == '__main__':
    unittest.main()