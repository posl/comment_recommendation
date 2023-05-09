def solve(n, m, k):
    MOD = 998244353
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(k + 1):
            for l in range(min(j, m) + 1):
                dp[i][j] += dp[i - 1][j - l]
                dp[i][j] %= MOD
    return dp[n][k]
