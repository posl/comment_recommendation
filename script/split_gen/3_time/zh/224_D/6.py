def dfs(v, p, c):
    if p == 8:
        if c == 8:
            return 0
        else:
            return float('inf')
    if c > 8:
        return float('inf')
    if dp[v][p][c] != -1:
        return dp[v][p][c]
    res = float('inf')
    for i in range(1, 10):
        if i == v:
            res = min(res, dfs(i, p + 1, c))
        else:
            res = min(res, dfs(i, p + 1, c + 1) + 1)
    dp[v][p][c] = res
    return res
M = int(input())
uv = [[int(i) for i in input().split()] for _ in range(M)]
p = [int(i) for i in input().split()]
dp = [[[-1 for _ in range(9)] for _ in range(9)] for _ in range(10)]
res = float('inf')
for i in range(1, 10):
    res = min(res, dfs(i, 0, 0))
print(res if res < float('inf') else -1)
