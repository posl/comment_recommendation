def solve(n, m, x, t, d):
    for i in range(x, n):
        t = t + d
    for i in range(0, m):
        t = t - d
    return t
n, m, x, t, d = map(int, input().split())
print(solve(n, m, x, t, d))
