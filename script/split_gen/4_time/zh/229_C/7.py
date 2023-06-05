def solve(n, w, a, b):
    #dp[i][j]表示用了前i种奶酪，总共用了j克奶酪时的美味度
    dp = [[0 for j in range(w+1)] for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, w+1):
            if j >= b[i-1]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-b[i-1]]+a[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][w]
