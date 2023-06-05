def getMinCost(h, w, c, a):
    #dp[i][j]表示在(i,j)建站的最小成本
    dp = [[0 for j in range(w)] for i in range(h)]
    #初始化
    dp[0][0] = a[0][0]
    for i in range(1, h):
        dp[i][0] = dp[i-1][0] + c*(i)
    for j in range(1, w):
        dp[0][j] = dp[0][j-1] + c*(j)
    #递推
    for i in range(1, h):
        for j in range(1, w):
            dp[i][j] = min(dp[i-1][j]+c*(i), dp[i][j-1]+c*(j), dp[i-1][j-1]+c*(i+j)) + a[i][j]
    return dp[h-1][w-1]
