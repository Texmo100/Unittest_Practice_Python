import unittest

# Test Fixture:
# A test fixture represents the preparation needed to perform 
# one or more tests and any associated cleanup actions.

class TestClassFixture(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # It is executed once Test Case starts
        print('Test Case "TestClassFixture" has started')

    @classmethod
    def tearDownClass(cls):
        # It is executed once Test Case finishes
        print('Test Case "TestClassFixture" has finished')

    def setUp(self):
        # It is executed before every test in Test Case
        print('Check {} has started.'.format(self._testMethodName))
    
    def tearDown(self):
        # It is executed after every test in Test Case
        print('Check {} has finished.'.format(self._testMethodName))

    def test_is_equal_to_1(self):
        a = 1
        self.assertEqual(a, 1)

    def test_30_in_sequence(self):
        self.assertIn(30, [10, 20, 30, 40, 50])
