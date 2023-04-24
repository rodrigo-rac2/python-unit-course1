# 1. Import unittest & the required module(s)
import unittest
import unittesting01
from unittesting01.tests.test_calculator import CalculatorTests
from unittesting01.tests.test_calculator_class import TestCalculator

# 2. Create an instance of the TestLoader
loader = unittest.TestLoader()

# 3. Create an instance of TestSuite
suite = unittest.TestSuite()

# 4. Add the test cases to the test suite instance
# >> Load the test cases from the test module(s)
suite.addTests(loader.loadTestsFromModule(unittesting01.tests.test_calculator))
suite.addTests(loader.loadTestsFromModule(unittesting01.tests.test_calculator_class))

# >> Load the test cases from the test class(es)
# suite.addTests(loader.loadTestsFromTestCase(CalculatorTests))
# suite.addTests(loader.loadTestsFromTestCase(TestCalculator))

# 5. Create an instance of the TextTestRunner
runner = unittest.TextTestRunner()

# 6. Run the TextTestRunner instance
test_results = runner.run(suite)

print("===================================")
print("Test suite 01 results:")
print("Tests run: ", test_results.testsRun)
print("Skipped: ", len(test_results.skipped))
print("Failures: ", len(test_results.failures))
print("Errors: ", len(test_results.errors))
print("Successful: ", test_results.wasSuccessful())
