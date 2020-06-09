"""
Program: coupon_calculations.py
Author: Spencer Cress
Date: 6/8

Function that calculates and returns price for Nestedif Assignment
"""

def calculate_price(price, cash_coupon, percent_coupon):
    shipping = 0
    tax = 1.06
    priceoff = price - cash_coupon
    #print(priceoff)
    discount = priceoff * (1-percent_coupon)
    #print(discount)
    if price <= 10:
        shipping = 5.95
    elif 10 < price <= 30:
        shipping = 7.95
    elif 30 < price <= 50:
        shipping = 11.95
    elif price > 50:
        shipping = 0
    #print(shipping)
    post_shipping = discount + shipping
    #print(post_shipping)
    final_price = post_shipping * tax
    #print(final_price)
    return final_price

if __name__ == '__main__':
    print_price = calculate_price(7.99,5,.1)
    print(print_price)
