def solve(N, C, D, color):
    # dp[i][j]: 1~i列，第i列的颜色为j时，最小错误度之和
    dp = [[float("inf") for i in range(C)] for j in range(N)]
    for i in range(C):
        dp[0][i] = 0
    for i in range(1, N):
        for j in range(C):
            for k in range(C):
                dp[i][j] = min(dp[i][j], dp[i - 1][k] + D[k][j])
    res = float("inf")
    for i in range(C):
        for j in range(C):
            res = min(res, dp[N - 1][i] + D[i][j] + dp[N - 1][j])
    return res
