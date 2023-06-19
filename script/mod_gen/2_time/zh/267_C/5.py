def solve(n, m, a):
    b = [0] * (n + 1)
    for i in range(n):
        b[i + 1] = b[i] + a[i]
    c = [0] * (n + 1)
    for i in range(n):
        c[i + 1] = max(c[i], b[i + 1])
    d = [0] * (n + 1)
    for i in range(n):
        d[i + 1] = max(d[i], c[i + 1] + b[i + 1])
    res = 0
    for i in range(1, m + 1):
        res = max(res, d[i] + b[i])
    return res
n, m = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, m, a))
