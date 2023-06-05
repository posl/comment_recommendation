def solve1(n, a, b):
    mod = 998244353
    dp = [[0] * 3001 for _ in range(3001)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(a[i], b[i] + 1):
            dp[i + 1][j] = dp[i][j] * (j - a[i] + 1) + dp[i + 1][j - 1] * (b[i] - j + 1)
            dp[i + 1][j] %= mod
    return dp[n][b[n - 1]]
