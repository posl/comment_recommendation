def solve(n, t, k, a):
    dp = [0] * (n + 1)
    for i in range(n):
        dp[i + 1] = dp[i] + t[i]
        for j in range(k[i]):
            dp[i + 1] = max(dp[i + 1], dp[a[i][j] - 1] + t[i])
    return dp[n]
