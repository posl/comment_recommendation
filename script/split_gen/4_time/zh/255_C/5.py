def solve(x, a, d, n):
    if n == 1:
        return 0
    if x < a:
        return a - x
    elif x > a + (n - 1) * d:
        return x - (a + (n - 1) * d)
    else:
        return 0
x, a, d, n = map(int, input().split())
print(solve(x, a, d, n))
