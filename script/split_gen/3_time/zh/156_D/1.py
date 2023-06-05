def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        r = a % b
        a = b
        b = r
    return a
n, a, b = map(int, input().split())
g = gcd(a, b)
a //= g
b //= g
m = min(a, b)
