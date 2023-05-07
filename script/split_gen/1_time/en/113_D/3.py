def solve(h, w, k):
    mod = 10 ** 9 + 7
    dp = [[0] * w for _ in range(h + 1)]
    dp[0][0] = 1
    for i in range(h):
        for j in range(w):
            if j == 0:
                dp[i + 1][j] = dp[i][j] * (w - 1)
                dp[i + 1][j + 1] = dp[i][j]
            elif j == w - 1:
                dp[i + 1][j] = dp[i][j] * (w - 1)
                dp[i + 1][j - 1] = dp[i][j]
            else:
                dp[i + 1][j] = dp[i][j] * (w - 2)
                dp[i + 1][j - 1] = dp[i][j]
                dp[i + 1][j + 1] = dp[i][j]
    return dp[h][k - 1] % mod
