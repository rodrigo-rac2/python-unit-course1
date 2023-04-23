import unittest
from unittesting02.calculator02 import Calculator

class TestCalculatorAddBase(unittest.TestCase):
    """
    A test class for the base functionality of Add method in the Calculator class.
    """
    def test_add(self):
        """
        Tests the add method of the Calculator class.
        """
        calc = Calculator(1, 2)
        self.assertEqual(calc.add(), 3)

class TestCalculatorAddAdditional(unittest.TestCase):
    """
    A test class for the additional functionality of Add method in the Calculator class.
    """
    def test_add_negative_numbers_in_the_input(self):
        """
        Test the add method by adding two negative numbers as input
        """
        calc = Calculator(-1, -2)
        self.assertEqual(calc.add(), -3)

    def test_add_two_negative_numbers(self):
        """
        Test the add method by adding two negative numbers
        """
        calc = Calculator(-1, -2)
        self.assertEqual(calc.add(), -3)

    def test_add_negative_numbers_in_the_output(self):
        """
        Test the add method by adding two positive numbers and getting a negative number as output
        """
        calc = Calculator(1, -2)
        self.assertEqual(calc.add(), -1)

    def test_add_two_positive_numbers(self):
        """
        Test the add method by adding two positive numbers
        """
        calc = Calculator(1, 2)
        self.assertEqual(calc.add(), 3)

    def test_add_zero_in_the_input(self):
        """
        Test the add method by adding zero as input
        """
        calc = Calculator(0, 2)
        self.assertEqual(calc.add(), 2)

    def test_add_zero_in_the_output(self):
        """
        Test the add method by adding zero as output
        """
        calc = Calculator(1, 0)
        self.assertEqual(calc.add(), 1)

    def test_add_float_numbers_in_the_input(self):
        """
        Test the add method by adding float numbers as input
        """
        calc = Calculator(1.5, 2.5)
        self.assertEqual(calc.add(), 4)

    def test_add_float_numbers_in_the_output(self):
        """
        Test the add method by adding float numbers as output
        """
        calc = Calculator(1.5, 2.5)
        self.assertEqual(calc.add(), 4)

    def test_add_string_in_the_input(self):
        """
        Test the add method by adding string as input
        """
        calc = Calculator('1', '2')
        self.assertEqual(calc.add(), '12')

    def test_add_string_in_the_output(self):
        """
        Test the add method by adding string as output
        """
        calc = Calculator('1', '2')
        self.assertEqual(calc.add(), '12')

    def test_add_list_in_the_input(self):
        """
        Test the add method by adding list as input
        """
        calc = Calculator([1, 2], [3, 4])
        self.assertEqual(calc.add(), [1, 2, 3, 4])

    def test_add_list_in_the_output(self):
        """
        Test the add method by adding list as output
        """
        calc = Calculator([1, 2], [3, 4])
        self.assertEqual(calc.add(), [1, 2, 3, 4])

    def test_add_tuple_in_the_input(self):
        """
        Test the add method by adding tuple as input
        """
        calc = Calculator((1, 2), (3, 4))
        self.assertEqual(calc.add(), (1, 2, 3, 4))

    def test_add_tuple_in_the_output(self):
        """
        Test the add method by adding tuple as output
        """
        calc = Calculator((1, 2), (3, 4))
        self.assertEqual(calc.add(), (1, 2, 3, 4))

    def test_add_bytes_in_the_input(self):
        """
        Test the add method by adding bytes as input
        """
        calc = Calculator(b'1', b'2')
        self.assertEqual(calc.add(), b'12')

    def test_add_bytes_in_the_output(self):
        """
        Test the add method by adding bytes as output
        """
        calc = Calculator(b'1', b'2')
        self.assertEqual(calc.add(), b'12')

    def test_add_bytearray_in_the_input(self):
        """
        Test the add method by adding bytearray as input
        """
        calc = Calculator(bytearray(b'1'), bytearray(b'2'))
        self.assertEqual(calc.add(), bytearray(b'12'))

    def test_add_bytearray_in_the_output(self):
        """
        Test the add method by adding bytearray as output
        """
        calc = Calculator(bytearray(b'1'), bytearray(b'2'))
        self.assertEqual(calc.add(), bytearray(b'12'))

    def test_add_complex_in_the_input(self):
        """
        Test the add method by adding complex as input
        """
        calc = Calculator(complex(1, 2), complex(3, 4))
        self.assertEqual(calc.add(), complex(4, 6))

    def test_add_complex_in_the_output(self):
        """
        Test the add method by adding complex as output
        """
        calc = Calculator(complex(1, 2), complex(3, 4))
        self.assertEqual(calc.add(), complex(4, 6))
