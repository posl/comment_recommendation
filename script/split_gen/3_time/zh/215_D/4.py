def gcd(x, y):
    if x < y:
        x, y = y, x
    while x % y != 0:
        x, y = y, x % y
    return y
