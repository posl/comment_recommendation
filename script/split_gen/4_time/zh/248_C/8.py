def dfs(n, m, k):
    if n == 0:
        return 1 if k == 0 else 0
    if dp[n][k] != -1:
        return dp[n][k]
    res = 0
    for i in range(1, m+1):
        if k-i >= 0:
            res += dfs(n-1, m, k-i)
    dp[n][k] = res
    return res
n, m, k = map(int, input().split())
dp = [[-1 for i in range(k+1)] for j in range(n+1)]
print(dfs(n, m, k))
