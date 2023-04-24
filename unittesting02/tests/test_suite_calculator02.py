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
import unittesting02
from unittesting02.tests.test_calculator02_01 import TestCalculator
from unittesting02.tests.test_add_calculator02 import TestCalculatorAddBase
from unittesting02.tests.test_add_calculator02 import TestCalculatorAddAdditional
from unittesting02.tests.test_setup_teardown_calculator02 import TestCalculatorSetupTeardown
from unittesting02.tests.test_skip_calculator02 import TestCalculatorSKip

# 2. Create an instance of the TestLoader
loader = unittest.TestLoader()

# 3. Create an instance of TestSuite
suite = unittest.TestSuite()

# 4. Add the test cases to the test suite instance
# >> Load the test cases from the test module(s)
# suite.addTests(loader.loadTestsFromModule(unittesting02.tests.test_calculator02_01))
# suite.addTests(loader.loadTestsFromModule(unittesting02.tests.test_add_calculator02))
# suite.addTests(loader.loadTestsFromModule(unittesting02.tests.test_setup_teardown_calculator02))
# suite.addTests(loader.loadTestsFromModule(unittesting02.tests.test_skip_calculator02))

# >> Load the test cases from the test class(es)
suite.addTests(loader.loadTestsFromTestCase(TestCalculator))
suite.addTests(loader.loadTestsFromTestCase(TestCalculatorAddBase))
suite.addTests(loader.loadTestsFromTestCase(TestCalculatorAddAdditional))
suite.addTests(loader.loadTestsFromTestCase(TestCalculatorSetupTeardown))
suite.addTests(loader.loadTestsFromTestCase(TestCalculatorSKip))

# 5. Create an instance of the TextTestRunner
runner = unittest.TextTestRunner()

# 6. Run the TextTestRunner instance
test_results = runner.run(suite)

print("===================================")
print("Test suite 02 results:")
print("Tests run: ", test_results.testsRun)
print("Skipped: ", len(test_results.skipped))
print("Failures: ", len(test_results.failures))
print("Errors: ", len(test_results.errors))
print("Successful: ", test_results.wasSuccessful())

