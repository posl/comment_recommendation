def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
a, b = map(int, input().split())

if __name__ == '__main__':
    gcd()