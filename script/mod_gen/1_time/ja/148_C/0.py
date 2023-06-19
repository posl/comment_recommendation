def gcd(x, y):
    if x < y:
        x, y = y, x
    if y == 0:
        return x
    else:
        return gcd(y, x%y)
a, b = map(int, input().split())
print(a*b//gcd(a, b))
