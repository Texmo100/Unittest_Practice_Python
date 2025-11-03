import unittest

# Test case:
# a single test unit with checks for a specific functionality

class TestClassTestCase(unittest.TestCase):

    def test_true_method(self):
        self.assertTrue(True)

    def test_is_in_sequence(self):
        self.assertIn(1, [1,2,3])

    def test_is_equal_to(self):
        a = b = 1
        self.assertEqual(a, b)

    def test_not_in_sequence(self):
        self.assertNotIn(1, [2,3,4])
