import unittest
from unittesting02.calculator02 import Calculator

class TestCalculatorSKip(unittest.TestCase):
    """
    A test class for the additional functionality of Add method in the Calculator class.
    """
    def test_add_two_negative_numbers(self):
        """
        Test the add method by adding two negative numbers
        """
        calc = Calculator(-1, -2)
        self.assertEqual(calc.add(), -3)

    def add_negative_numbers_in_the_output(self):
        """
        :return:rhis will be ignored - doesn't start with `test`
        """
        calc = Calculator(1, -2)
        self.assertEqual(calc.add(), -1)

    def test_add_two_positive_numbers(self):
        """
        :return:this will always pass
        """
        pass

    @unittest.skip("This test is skipped")
    def test_add_zero_in_the_input(self):
        """
        :return:this will be skipped
        """
        calc = Calculator(0, 2)
        self.assertEqual(calc.add(), 2)

    def test_add_zero_in_the_output(self):
        """
        Test the add method by adding zero as output
        """
        calc = Calculator(1, 0)
        self.assertEqual(calc.add(), 1)

    @unittest.skip("This test is skipped")
    def test_add_float_numbers_in_the_input(self):
        """
        Test the add method by adding float numbers as input
        """
        calc = Calculator(1.5, 2.5)
        self.assertEqual(calc.add(), 4)

    def test_add_complex_in_the_input(self):
        """
        Test the add method by adding complex as input
        """
        calc = Calculator(complex(1, 2), complex(3, 4))
        self.assertEqual(calc.add(), complex(4, 6))

    @unittest.skip("This test is skipped")
    def test_add_complex_in_the_output(self):
        """
        Test the add method by adding complex as output
        """
        calc = Calculator(complex(1, 2), complex(3, 4))
        self.assertEqual(calc.add(), complex(4, 6))
