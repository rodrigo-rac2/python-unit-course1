import unittest
import calculator


class CalculatorTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.calc_add(1, 2), 3)
        self.assertEqual(calculator.calc_add(2, 2), 4)
        self.assertEqual(calculator.calc_add(3, 2), 5)

    def test_sub(self):
        self.assertEqual(calculator.calc_sub(1, 2), -1)
        self.assertEqual(calculator.calc_sub(2, 2), 0)
        self.assertEqual(calculator.calc_sub(3, 2), 1)
