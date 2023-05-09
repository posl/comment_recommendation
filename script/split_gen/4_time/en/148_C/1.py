def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
a, b = map(int, input().split())
print(a*b//gcd(a, b))
