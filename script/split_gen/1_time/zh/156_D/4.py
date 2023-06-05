def gcd(a, b):
    if a > b:
        a, b = b, a
    while a > 0:
        a, b = b % a, a
    return b
