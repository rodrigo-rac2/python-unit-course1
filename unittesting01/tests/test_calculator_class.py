import unittest
from unittesting01.calculator_class import Calculator


class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator(1, 2)
        self.assertEqual(calc.add(), 3)

    def test_add_negative_numbers_in_the_input(self):
        calc = Calculator(-1, -2)
        self.assertEqual(calc.add(), -3)

    def test_add_two_negative_numbers(self):
        calc = Calculator(-1, -2)
        self.assertEqual(calc.add(), -3)

    def test_add_negative_numbers_in_the_output(self):
        calc = Calculator(1, -2)
        self.assertEqual(calc.add(), -1)

    def test_add_decimals_in_the_input(self):
        calc = Calculator(10, 20)
        self.assertEqual(calc.add(), 30)

    def test_add_hundreds_in_the_input(self):
        calc = Calculator(100, 200)
        self.assertEqual(calc.add(), 300)

    def test_add_thousands_in_the_input(self):
        calc = Calculator(1000, 2000)
        self.assertEqual(calc.add(), 3000)

    def test_add_millions_in_the_input(self):
        calc = Calculator(1000000, 2000000)
        self.assertEqual(calc.add(), 3000000)

    def test_sub(self):
        calc = Calculator(1, 2)
        self.assertEqual(calc.sub(), -1)

    def test_sub_negative_numbers_in_the_input(self):
        calc = Calculator(-1, -2)
        self.assertEqual(calc.sub(), 1)

    def test_sub_two_negative_numbers(self):
        calc = Calculator(-1, -2)
        self.assertEqual(calc.sub(), 1)

    def test_sub_negative_numbers_in_the_output(self):
        calc = Calculator(1, -2)
        self.assertEqual(calc.sub(), 3)

    def test_sub_decimals_in_the_input(self):
        calc = Calculator(10, 20)
        self.assertEqual(calc.sub(), -10)

    def test_sub_hundreds_in_the_input(self):
        calc = Calculator(100, 200)
        self.assertEqual(calc.sub(), -100)

    def test_sub_thousands_in_the_input(self):
        calc = Calculator(1000, 2000)
        self.assertEqual(calc.sub(), -1000)

    def test_sub_millions_in_the_input(self):
        calc = Calculator(1000000, 2000000)
        self.assertEqual(calc.sub(), -1000000)
