def gcd(x, y):
    if x == 0 or y == 0:
        return 0
    while y != 0:
        r = x % y
        x = y
        y = r
    return x
