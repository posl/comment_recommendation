def findValidAmidakuji(h,w,k):
    #h:垂直线的个数
    #w:水平线的个数
    #k:最后一条水平线的位置
    #dp[i][j]:最后一条水平线的位置为j且第i条垂直线的位置为j-1的情况下的有效羊皮卷的个数
    dp = [[0 for i in range(w+1)] for j in range(h+1)]
    dp[0][1] = 1
    for i in range(1,h+1):
        for j in range(1,w+1):
            if j > 1:
                dp[i][j] += dp[i-1][j-1]
            if j < w:
                dp[i][j] += dp[i-1][j+1]
            dp[i][j] %= 1000000007
    return dp[h][k]
