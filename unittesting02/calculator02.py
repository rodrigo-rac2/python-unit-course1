class Calculator:
    """
    A simple calculator class.
    Constructor requires two numbers: number1 and number 2.
    """
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def add(self):
        """
        Adds the two numbers, and returns the result.
        :return: number1 + number2
        """
        return self.number1 + self.number2

    def sub(self):
        """
        Subtracts the two numbers, and returns the result.
        :return: number1 - number2
        """
        return self.number1 - self.number2

    def mul(self):
        """
        Multiplies the two numbers, and returns the result.
        :return: number1 * number2
        """
        return self.number1 * self.number2

    def div(self):
        """
        Divides the two numbers, and returns the result.
        :return: number1 / number2
        """
        return self.number1 / self.number2

    def mod(self):
        """
        Divides the two numbers, and returns the remainder.
        :return: number1 % number2
        """
        return self.number1 % self.number2

    def pow(self):
        """
        Raises the first number to the power of the second number.
        :return: number1 ** number2
        """
        return self.number1 ** self.number2

    def sqrt(self):
        """
        Returns the square root of the first number.
        :return: number1 ** 0.5
        """
        return self.number1 ** 0.5

    def cbrt(self):
        """
        Returns the cube root of the first number.
        :return: number1 ** (1/3)
        """
        return self.number1 ** (1/3)

    if __name__ == '__main__':
        print("Imported module02.calculator02.py")
