def solve(h, w, k):
    if w == 1:
        return 1
    MOD = 10 ** 9 + 7
    dp = [[0] * w for _ in range(h + 1)]
    dp[0][0] = 1
    for i in range(h):
        for j in range(w):
            if j == 0:
                dp[i + 1][j] = dp[i][j + 1]
            elif j == w - 1:
                dp[i + 1][j] = dp[i][j - 1]
            else:
                dp[i + 1][j] = dp[i][j - 1] + dp[i][j + 1]
    return dp[h][k - 1] % MOD
