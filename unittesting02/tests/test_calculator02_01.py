import unittest
from unittesting02.calculator02 import Calculator

class TestCalculator(unittest.TestCase):
    """
    A test class for the base functionality of the Calculator class.
    """
    def test_add(self):
        """
        Tests the add method of the Calculator class.
        """
        calc = Calculator(1, 2)
        self.assertEqual(calc.add(), 3)


    def test_sub(self):
        """
        Tests the sub method of the Calculator class.
        """
        calc = Calculator(1, 2)
        self.assertEqual(calc.sub(), -1)

    def test_mul(self):
        """
        Tests the mul method of the Calculator class.
        """
        calc = Calculator(1, 2)
        self.assertEqual(calc.mul(), 2)

    def test_div(self):
        """
        Tests the div method of the Calculator class.
        """
        calc = Calculator(1, 2)
        self.assertEqual(calc.div(), 0.5)

    def test_mod(self):
        """
        Tests the mod method of the Calculator class.
        """
        calc = Calculator(1, 2)
        self.assertEqual(calc.mod(), 1)

    def test_pow(self):
        """
        Tests the pow method of the Calculator class.
        """
        calc = Calculator(4, 2)
        self.assertEqual(calc.pow(), 16)

    def test_sqrt(self):
        """
        Tests the sqrt method of the Calculator class.
        """
        calc = Calculator(2, 3)
        self.assertEqual(calc.sqrt(), 1.4142135623730951)

    def test_cbrt(self):
        """
        Tests the cbrt method of the Calculator class.
        """
        calc = Calculator(5, 2)
        self.assertEqual(calc.cbrt(), 1.7099759466766968)
