"""
Program: validation_with_try.py
Author: Spencer Cress
Date: 6/9

Student average scores function for assignment
"""


def average(score1, score2, score3):
    try:
        if score1 < 0:
            raise ValueError
        if score2 < 0:
            raise ValueError
        if score3 < 0:
            raise ValueError
    except:
        print("A value entered is negative, please select valid input.")
    NUMBER_TESTS = 3
    return float((score1 + score2 + score3)/NUMBER_TESTS)


if __name__ == '__main__':
    print(average(-90,82,3))
