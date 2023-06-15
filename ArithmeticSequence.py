from math import floor, sqrt


class ArithmeticSequence:
    def __init__(self, sequence):
        self.value = floor(sequence * sqrt(2))
