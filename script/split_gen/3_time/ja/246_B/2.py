def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
A, B = map(int, input().split())
g = gcd(A, B)
print(A/g, B/g)
