import unittest

from sum_func import sumCubes
from fractions import Fraction

class TestSumCubes(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sumCubes(data)
        self.assertEqual(result, 36)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 2), Fraction(1, 2), Fraction(3, 4)]
        result = sumCubes(data)
        self.assertEqual(result, Fraction(43, 64))

    def test_bad_type(self):
        data = "banana"
        with self.assertRaises(TypeError):
            result = sumCubes(data)

if __name__ == '__main__':
    unittest.main()