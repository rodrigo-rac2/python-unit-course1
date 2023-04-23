"""
    Test suite >>>>
        A test suite is a collection of test cases, test suites, or both.
        It is used to aggregate tests that should be executed together.
    Test runner >>>>
        A test runner is a component which orchestrates the execution of tests and
        provides the outcome to the user. The runner may use a graphical interface,
        a textual interface, or return a special value to indicate the results of
        executing the tests.
"""

# 1. Import unittest & the required module(s)
import unittest
from unittesting02.tests.test_calculator02_01 import TestCalculator
from unittesting02.tests.test_add_calculator02 import TestCalculatorAddBase
from unittesting02.tests.test_add_calculator02 import TestCalculatorAddAdditional
from unittesting02.tests.test_setup_teardown_calculator02 import TestCalculatorSetupTeardown
from unittesting02.tests.test_skip_calculator02 import TestCalculatorSKip

# 2. Create an instance of the TestLoader

# 3. Create an instance of TestSuite

# 4. Add the test cases to the test suite instance
# >> Load the test cases from the test module(s)

# 5. Create an instance of the TextTestRunner

# 6. Run the TextTestRunner instance
