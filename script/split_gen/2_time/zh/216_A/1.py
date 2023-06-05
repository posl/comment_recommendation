def gcd(x, y):
    if x < y:
        x, y = y, x
    while y != 0:
        r = x % y
        x = y
        y = r
    return x
N, M = map(int, input().split())
A = list(map(int, input().split()))
max_A = max(A)
max_M = max(M, max_A)
