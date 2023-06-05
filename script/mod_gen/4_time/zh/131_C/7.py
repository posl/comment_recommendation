def gcd(m, n):
    if m < n:
        m, n = n, m
    while n != 0:
        m, n = n, m % n
    return m

if __name__ == '__main__':
    gcd()