import unittest

from ArithmeticSequence import ArithmeticSequence


def isNotLinear(difference1, difference2):
    return difference1 == difference2


class ArithmeticSumDifferencesTest(unittest.TestCase):
    def test_getArithmeticSumDifference(self):
        assert ArithmeticSequence(2).value - ArithmeticSequence(1).value > 0 
        
    def test_showArithmeticSumDifferenceIsNotLinear(self):
        difference1 = ArithmeticSequence(2).value - ArithmeticSequence(1).value
        difference2 = ArithmeticSequence(3).value - ArithmeticSequence(2).value
        assert not isNotLinear(difference1, difference2)


if __name__ == '__main__':
    unittest.main()
