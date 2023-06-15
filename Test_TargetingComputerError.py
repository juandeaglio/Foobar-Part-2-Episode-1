import unittest

from ArithmeticSum import ArithmeticSum


class ArithmeticSumTest(unittest.TestCase):
    def test_arithmeticSumOfOne(self):
        self.assertEqual(1, ArithmeticSum(1).sumValue)

    def test_arithmeticSumOfTwo(self):
        self.assertEqual(3, ArithmeticSum(2).sumValue)

    def test_arithmeticSumOfFiveself(self):
        self.assertEqual(19, ArithmeticSum(5).sumValue)


if __name__ == '__main__':
    unittest.main()
