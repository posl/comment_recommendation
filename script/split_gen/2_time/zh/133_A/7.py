def func(n, k):
    # dp[i][j]表示前i个球中有j个蓝球的方案数
    dp = [[0 for i in range(k+1)] for j in range(n+1)]
    dp[1][1] = 1
    dp[1][0] = 1
    for i in range(2, n+1):
        for j in range(k+1):
            if j == 0:
                dp[i][j] = dp[i-1][j+1]
            elif j == k:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j+1] + dp[i-1][j-1]
    return dp[n][k]
