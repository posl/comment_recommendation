def solve(n,m,x,c,y):
    #dp[i][j]表示第i次投掷，连胜奖金为j时的最大金额
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n):
        for j in range(n+1):
            dp[i+1][j] = max(dp[i+1][j],dp[i][j])
            if j < m and c[j] == i+1:
                dp[i+1][j+1] = max(dp[i+1][j+1],dp[i][j]+y[j])
            dp[i+1][0] = max(dp[i+1][0],dp[i][j]+x[i])
    return max(dp[n])

if __name__ == '__main__':
    solve()