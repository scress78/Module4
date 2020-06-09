def average(score1, score2, score3):
    if score1 < 0:
        raise ValueError
    if score2 < 0:
        raise ValueError
    NUMBER_TESTS = 3
    return float((score1 + score2 + score3)/NUMBER_TESTS)

if __name__ == '__main__':
    print(average(-90,82,3))
