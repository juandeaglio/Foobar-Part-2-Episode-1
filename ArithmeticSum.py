from ArithmeticSequence import ArithmeticSequence


class ArithmeticSum:
    def __init__(self, iterations):
        self.sumValue = self.calculateSum(iterations)

    def calculateSum(self, maxIterations):
        sumOfSequences = 0
        for i in range(1, maxIterations+1):
            sumOfSequences += ArithmeticSequence(i).value
        return sumOfSequences
