import unittest

from sum_func import sumSquares
from fractions import Fraction

class TestSumSquares(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [13546456, 45786692, 34574753]
        result = sumSquares(data)
        self.assertEqual(result, 3475341179473809)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(179780, 2780980), Fraction(34561, 2457), Fraction(33457, 4573)]
        result = sumSquares(data)
        self.assertEqual(result, Fraction(613622931770304466486457851, 2440891390237738415243721))

    def test_bad_type(self):
        data = "banana"
        with self.assertRaises(TypeError):
            result = sumSquares(data)

if __name__ == '__main__':
    unittest.main()