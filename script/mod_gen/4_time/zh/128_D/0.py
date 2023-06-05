def solve(n, k, v):
    res = 0
    for i in range(min(k, n) + 1):
        for j in range(min(k - i, n - i) + 1):
            l = v[:i] + v[n - j:]
            res = max(res, sum(l))
    return res
n, k = map(int, input().split())
v = list(map(int, input().split()))
print(solve(n, k, v))
