import unittest
import calculator


class CalculatorTests(unittest.TestCase):
    def test_add_basic(self):
        self.assertEqual(calculator.calc_add(1, 2), 3)
        self.assertEqual(calculator.calc_add(2, 2), 4)
        self.assertEqual(calculator.calc_add(3, 2), 5)

    def test_add_negative_numbers_in_the_input(self):
        self.assertEqual(calculator.calc_add(-1, -2), -3)
        self.assertEqual(calculator.calc_add(-2, 2), 0)
        self.assertEqual(calculator.calc_add(-3, 2), -1)

    def test_add_two_negative_numbers(self):
        self.assertEqual(calculator.calc_add(-1, -2), -3)
        self.assertEqual(calculator.calc_add(-2, -2), -4)
        self.assertEqual(calculator.calc_add(-3, -2), -5)

    def test_add_negative_numbers_in_the_output(self):
        self.assertEqual(calculator.calc_add(1, -2), -1)
        self.assertEqual(calculator.calc_add(2, -2), 0)
        self.assertEqual(calculator.calc_add(3, -2), 1)

    def test_add_decimals_in_the_input(self):
        self.assertEqual(calculator.calc_add(10, 20), 30)
        self.assertEqual(calculator.calc_add(20, 20), 40)
        self.assertEqual(calculator.calc_add(30, 20), 50)

    def test_add_hundreds_in_the_input(self):
        self.assertEqual(calculator.calc_add(100, 200), 300)
        self.assertEqual(calculator.calc_add(200, 200), 400)
        self.assertEqual(calculator.calc_add(300, 200), 500)

    def test_add_thousands_in_the_input(self):
        self.assertEqual(calculator.calc_add(1000, 2000), 3000)
        self.assertEqual(calculator.calc_add(2000, 2000), 4000)
        self.assertEqual(calculator.calc_add(3000, 2000), 5000)

    def test_add_millions_in_the_input(self):
        self.assertEqual(calculator.calc_add(1000000, 2000000), 3000000)
        self.assertEqual(calculator.calc_add(2000000, 2000000), 4000000)
        self.assertEqual(calculator.calc_add(3000000, 2000000), 5000000)

    def test_add_billions_in_the_input(self):
        self.assertEqual(calculator.calc_add(1000000000, 2000000000), 3000000000)
        self.assertEqual(calculator.calc_add(2000000000, 2000000000), 4000000000)
        self.assertEqual(calculator.calc_add(3000000000, 2000000000), 5000000000)

    def test_sub_basic(self):
        self.assertEqual(calculator.calc_sub(1, 2), -1)
        self.assertEqual(calculator.calc_sub(2, 2), 0)
        self.assertEqual(calculator.calc_sub(3, 2), 1)

    def test_sub_negative_numbers_in_the_input(self):
        self.assertEqual(calculator.calc_sub(-1, -2), 1)
        self.assertEqual(calculator.calc_sub(-2, 2), -4)
        self.assertEqual(calculator.calc_sub(-3, 2), -5)

    def test_sub_two_negative_numbers(self):
        self.assertEqual(calculator.calc_sub(-1, -2), 1)
        self.assertEqual(calculator.calc_sub(-2, -2), 0)
        self.assertEqual(calculator.calc_sub(-3, -2), -1)

    def test_sub_negative_numbers_in_the_output(self):
        self.assertEqual(calculator.calc_sub(1, -2), 3)
        self.assertEqual(calculator.calc_sub(2, -2), 4)
        self.assertEqual(calculator.calc_sub(3, -2), 5)

    def test_sub_decimals_in_the_input(self):
        self.assertEqual(calculator.calc_sub(10, 20), -10)
        self.assertEqual(calculator.calc_sub(20, 20), 0)
        self.assertEqual(calculator.calc_sub(30, 20), 10)

    def test_sub_hundreds_in_the_input(self):
        self.assertEqual(calculator.calc_sub(100, 200), -100)
        self.assertEqual(calculator.calc_sub(200, 200), 0)
        self.assertEqual(calculator.calc_sub(300, 200), 100)

    def test_sub_thousands_in_the_input(self):
        self.assertEqual(calculator.calc_sub(1000, 2000), -1000)
        self.assertEqual(calculator.calc_sub(2000, 2000), 0)
        self.assertEqual(calculator.calc_sub(3000, 2000), 1000)

    def test_sub_millions_in_the_input(self):
        self.assertEqual(calculator.calc_sub(1000000, 2000000), -1000000)
        self.assertEqual(calculator.calc_sub(2000000, 2000000), 0)
        self.assertEqual(calculator.calc_sub(3000000, 2000000), 1000000)

    def test_sub_billions_in_the_input(self):
        self.assertEqual(calculator.calc_sub(1000000000, 2000000000), -1000000000)
        self.assertEqual(calculator.calc_sub(2000000000, 2000000000), 0)
        self.assertEqual(calculator.calc_sub(3000000000, 2000000000), 1000000000)
