def gcd(a, b): return a if b == 0 else gcd(b, a % b)

if __name__ == '__main__':
    gcd()