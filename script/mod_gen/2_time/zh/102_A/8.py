def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)
n = int(input())
print(n * 2 // gcd(2, n))
