def gcd(a, b):
    if a < b:
        a, b = b, a
    if a % b:
        return gcd(b, a % b)
    else:
        return b
