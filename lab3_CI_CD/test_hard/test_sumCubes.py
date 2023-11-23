import unittest

from sum_func import sumCubes
from fractions import Fraction

class TestSumCubes(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [46435645, -456452, 354746764845683]
        result = sumCubes(data)
        self.assertEqual(result, 44643201399158327045089511716040383090970704)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1456, 4562), Fraction(176, 2567), Fraction(3457, 4457)]
        result = sumCubes(data)
        self.assertEqual(result, Fraction(8877320535141391675803359407775, 17773844001283263275484790900519))

    def test_bad_type(self):
        data = "banana"
        with self.assertRaises(TypeError):
            result = sumCubes(data)

if __name__ == '__main__':
    unittest.main()