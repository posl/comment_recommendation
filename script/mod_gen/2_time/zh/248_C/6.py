def solve(n,m,k):
    dp = [[0]*(k+1) for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1,n+1):
        for j in range(1,k+1):
            for l in range(1,m+1):
                if j-l >= 0:
                    dp[i][j] += dp[i-1][j-l]
    return dp[n][k]

if __name__ == '__main__':
    solve()