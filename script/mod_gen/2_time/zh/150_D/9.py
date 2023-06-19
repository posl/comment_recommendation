def gcd(m,n):
    if n == 0:
        return m
    else:
        return gcd(n, m%n)

if __name__ == '__main__':
    gcd()