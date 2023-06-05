def solve(n,m,a):
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i<j:
                dp[i][j] = -100000000
            else:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]+a[i-1]*j)
    return dp[n][m]

if __name__ == '__main__':
    solve()