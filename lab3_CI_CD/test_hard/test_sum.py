import unittest

from sum_func import sum
from fractions import Fraction

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [7349593490384609, 898345698734560980394, 34586978606789, 32463457568579]
        result = sum(data)
        self.assertEqual(result, 898353115378487540371)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(143564357, 43457), Fraction(1346, 42346), Fraction(2364, 5346)]
        result = sum(data)
        self.assertEqual(result, Fraction(2708750708527936, 819822519351))

    def test_bad_type(self):
        data = "banana"
        with self.assertRaises(TypeError):
            result = sum(data)

if __name__ == '__main__':
    unittest.main()