def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
k = int(input())
g = gcd(k, 10)
