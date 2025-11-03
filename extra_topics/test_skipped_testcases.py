import unittest
import sys

class SkippedTestCases(unittest.TestCase):
    @unittest.skip("Demonstrating skipping")
    def test_nothing(self):
        # Test should not be executed in any case
        # self.fail() - method that fails
        # test with text in brackets

        self.fail("Shouldn't happen")

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # Test should be skipped if OS is not Windows
        pass

@unittest.skip("Whole Test Case skipping")
class SkippedWholeTestCase(unittest.TestCase):
    def test_not_run(self):
        pass
