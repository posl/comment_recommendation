def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)
N = int(input())
A = list(map(int, input().split()))
