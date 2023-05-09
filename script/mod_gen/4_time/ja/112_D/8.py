def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
n, m = map(int, input().split())
a = [m // n] * n

if __name__ == '__main__':
    gcd()