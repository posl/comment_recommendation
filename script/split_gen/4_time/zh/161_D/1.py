def check(x):
    if x < 10:
        return True
    if x < 100:
        return abs(x // 10 - x % 10) <= 1
    return abs(x // 10 % 10 - x % 10) <= 1 and check(x // 10)
