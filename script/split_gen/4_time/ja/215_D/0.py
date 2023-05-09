def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
n, m = map(int, input().split())
a = list(map(int, input().split()))
