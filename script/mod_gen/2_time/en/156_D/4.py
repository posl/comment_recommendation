def combination(n, r, mod):
    if r < 0 or n < r:
        return 0
    if n - r < r:
        r = n - r
    if r == 0:
        return 1
    if r == 1:
        return n
    numerator = 1
    denominator = 1
    for i in range(1, r + 1):
        numerator = numerator * (n - i + 1) % mod
        denominator = denominator * i % mod
    return numerator * pow(denominator, mod - 2, mod) % mod

if __name__ == '__main__':
    combination()