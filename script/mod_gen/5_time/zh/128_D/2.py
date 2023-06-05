def dp(n, k, v):
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
    for i in range(n):
        for j in range(k+1):
            if j == 0:
                dp[i+1][j] = dp[i][j] + v[i]
            else:
                dp[i+1][j] = max(dp[i][j] + v[i], dp[i][j-1])
    return dp[n][k]
n, k = map(int, input().split())
v = list(map(int, input().split()))
print(dp(n, k, v))
