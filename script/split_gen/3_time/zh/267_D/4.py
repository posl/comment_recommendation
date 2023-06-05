def get_max_sum(n,m,nums):
    dp = [[0 for j in range(m+1)] for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]+i*nums[i-1])
    return dp[n][m]
