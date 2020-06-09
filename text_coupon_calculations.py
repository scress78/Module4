"""
Program: test_coupon_calculations.py
Author: Spencer Cress
Date: 6/8

This program tests the coupon codes for this week's assignment
"""

from store import coupon_calculations as cc
import unittest
import unittest.mock as mock


class MyTestCase(unittest.TestCase):
    #def calculate_price(price, cash_coupon, percent_coupon):
    def test_price_under_10(self):
        value_under_ten = 7.99
        self.assertAlmostEqual(cc.calculate_price(value_under_ten, 5, .1), 9.16, places=2)
        self.assertAlmostEqual(cc.calculate_price(value_under_ten, 5, .15), 9.00, places=2)
        self.assertAlmostEqual(cc.calculate_price(value_under_ten, 5, .2), 8.84, places=2)
        self.assertAlmostEqual(cc.calculate_price(value_under_ten, 10, .1), 4.39, places=2)
        self.assertAlmostEqual(cc.calculate_price(value_under_ten, 10, .15), 4.5, places=2)
        self.assertAlmostEqual(cc.calculate_price(value_under_ten, 10, .20), 4.6, places=2)
    def test_price_under_between_ten_thirty(self):
        value_ten_to_thirty = 16.99
        self.assertAlmostEqual(cc.calculate_price(value_ten_to_thirty, 5, .1), 19.87, places=2)
        self.assertAlmostEqual(cc.calculate_price(value_ten_to_thirty, 5, .15), 19.23, places=2)
        self.assertAlmostEqual(cc.calculate_price(value_ten_to_thirty, 5, .2), 18.59, places=2)
        self.assertAlmostEqual(cc.calculate_price(value_ten_to_thirty, 10, .1), 15.1, places=2)
        self.assertAlmostEqual(cc.calculate_price(value_ten_to_thirty, 10, .15), 14.72, places=2)
        self.assertAlmostEqual(cc.calculate_price(value_ten_to_thirty, 10, .20), 14.35, places=2)
    def test_price_under_between_thirty_fifty(self):
        value_thirty_to_fifty = 39.99
        self.assertAlmostEqual(cc.calculate_price(value_thirty_to_fifty, 5, .1), 46.05, places=2)
        self.assertAlmostEqual(cc.calculate_price(value_thirty_to_fifty, 5, .15), 44.19, places=2)
        self.assertAlmostEqual(cc.calculate_price(value_thirty_to_fifty, 5, .2), 42.34, places=2)
        self.assertAlmostEqual(cc.calculate_price(value_thirty_to_fifty, 10, .1), 41.28, places=2)
        self.assertAlmostEqual(cc.calculate_price(value_thirty_to_fifty, 10, .15), 39.69, places=2)
        self.assertAlmostEqual(cc.calculate_price(value_thirty_to_fifty, 10, .20), 38.1, places=2)

if __name__ == '__main__':
    unittest.main()

