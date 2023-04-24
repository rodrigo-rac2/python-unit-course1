import unittest
from unittesting02.calculator02 import Calculator


class TestCalculatorSetupTeardown(unittest.TestCase):
    """
    A test class for the additional functionality of Add method in the Calculator class.
    """

    # def setUp(self):
    #     print("Running setUp")
    #
    # def tearDown(self):
    #     print("Running tearDown")

    def test_add_two_negative_numbers(self):
        # print("Running test_add_two_negative_numbers")
        calc = Calculator(-1, -2)
        self.assertEqual(calc.add(), -3)

    def test_add_negative_numbers_in_the_output(self):
        # print("Running test_add_negative_numbers_in_the_output")
        calc = Calculator(1, -2)
        self.assertEqual(calc.add(), -1)

    def test_add_zero_in_the_input(self):
        # print("Running test_add_zero_in_the_input")
        calc = Calculator(0, 2)
        self.assertEqual(calc.add(), 2)

    def test_add_complex_in_the_input(self):
        # print("Running test_add_complex_in_the_input")
        calc = Calculator(complex(1, 2), complex(3, 4))
        self.assertEqual(calc.add(), complex(4, 6))
