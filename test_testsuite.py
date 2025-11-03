import unittest
from .test_testcase import TestClassTestCase
from .test_fixture import TestClassFixture

# Test Suite:
# In the unittest framework, a test suite is a way of grouping test cases.

# Way #1
suite_1 = unittest.TestSuite()

suite_1.addTest(unittest.makeSuite(TestClassTestCase))

# Way #2
suite_2 = unittest.TestSuite()
suite_2.addTest(TestClassFixture())

# Adding an extra TestCase class to an existing Test Suite
class AnotherTestCase(unittest.TestCase):
    def test_me(self):
        self.suite_2.assertEqual(1, 2)

suite_2.addTest(unittest.makesuite(AnotherTestCase))

# Adding Test Suites to another Test Suite
suite_3 = unittest.TestSuite()
suite_3.addTests([suite_1, suite_2])
