def solve(x,y):
    mod = 10**9+7
    dp = [[0 for i in range(y+1)] for j in range(x+1)]
    dp[0][0] = 1
    for i in range(1,x+1):
        dp[i][0] = dp[i-1][0]
    for j in range(1,y+1):
        dp[0][j] = dp[0][j-1]
    for i in range(1,x+1):
        for j in range(1,y+1):
            dp[i][j] = (dp[i-1][j]+dp[i][j-1])%mod
    print(dp[x][y])

if __name__ == '__main__':
    solve()