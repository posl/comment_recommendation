def gcd(a, b):
    if a < b:
        a, b = b, a
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b

if __name__ == '__main__':
    gcd()