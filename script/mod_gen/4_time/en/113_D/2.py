def solve(h,w,k):
    dp = [[0 for i in range(w+1)] for j in range(h+1)]
    dp[0][1] = 1
    for i in range(1,h+1):
        for j in range(1,w+1):
            dp[i][j] += dp[i-1][j]*dp[i][j-1]
            dp[i][j] %= mod
            dp[i][j] += dp[i-1][j-1]*dp[i][j]
            dp[i][j] %= mod
    return dp[h][k]

if __name__ == '__main__':
    solve()