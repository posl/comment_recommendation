def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

if __name__ == '__main__':
    gcd()