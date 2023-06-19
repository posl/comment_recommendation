def gcd(n, m):
    if n < m:
        n, m = m, n
    while m != 0:
        n, m = m, n % m
    return n
