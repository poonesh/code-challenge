import unittest
from challenge1 import allEvenDigits


class Challenge1_Test(unittest.TestCase):

    def test_numbers_10_10(self):
        self.assertEqual(allEvenDigits(10, 10), [])

    def test_numbers_0_5(self):
        self.assertEqual(allEvenDigits(0, 5), [0, 2, 4])

    def test_numbers_10_20(self):
        self.assertEqual(allEvenDigits(10, 20), [20])

    def test_numbers_10_100(self):
        self.assertEqual(allEvenDigits(10, 100), [
        	20, 22, 24, 26, 28, 
        	40, 42, 44, 46, 48, 
        	60, 62, 64, 66, 68, 
        	80, 82, 84, 86, 88
        ])


if __name__ == '__main__':
    unittest.main()
