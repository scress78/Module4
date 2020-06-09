"""
Program: test_validation_with_try.py
Author: Spencer Cress
Date: 6/9

This program tests validation with try for a module 4 assignement
"""

import unittest
from input_validation.validation_with_try import average

class MyTestCase(unittest.TestCase):
    def test_average_exception(self):
        with self.assertRaises(ValueError):
            average(-90, 89, 78)
    def test_average_exception(self):
        with self.assertRaises(ValueError):
            average(90,- 89, 78)
    def test_average_exception(self):
        with self.assertRaises(ValueError):
            average(90, 89, -78)


if __name__ == '__main__':
    unittest.main()
