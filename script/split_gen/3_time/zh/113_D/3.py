def amidakuji(h,w,k):
    #h为垂直线条数
    #w为水平线条数
    #k为水平线条目标位置
    #dp=[[[0 for i in range(w)] for j in range(h)] for k in range(w)]
    dp=[[[0 for i in range(w)] for j in range(h)] for k in range(w)]
    dp[0][0][0]=1
    for i in range(h):
        for j in range(w):
            for k in range(w):
                if j==0 and k==0:
                    dp[i][j][k]=1
                elif j==0:
                    dp[i][j][k]=dp[i-1][j][k-1]+dp[i-1][j][k]+dp[i-1][j][k+1]
                elif k==0:
                    dp[i][j][k]=dp[i-1][j-1][k]+dp[i-1][j][k]+dp[i-1][j+1][k]
                else:
                    dp[i][j][k]=dp[i-1][j-1][k]+dp[i-1][j][k]+dp[i-1][j+1][k]+dp[i-1][j][k-1]+dp[i-1][j][k+1]
    return dp[h-1][w-1][k-1]
