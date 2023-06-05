def findS(s):
    dp = [[0 for i in range(s+1)] for j in range(s+1)]
    dp[0][0] = 1
    for i in range(3,s+1):
        for j in range(s+1):
            if j >= i:
                dp[i][j] = dp[i-1][j] + dp[i][j-i]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[s][s] % (10**9+7)
