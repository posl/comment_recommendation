def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
N, X = map(int, input().split())
x = list(map(int, input().split()))
x.append(X)
x.sort()
