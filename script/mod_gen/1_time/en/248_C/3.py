def solve(n,m,k):
    dp = [[[0 for _ in range(k+1)] for _ in range(m+1)] for _ in range(n+1)]
    dp[0][0][0] = 1
    for i in range(n):
        for j in range(m):
            for l in range(k):
                dp[i+1][j+1][l+1] += dp[i][j][l]
                dp[i+1][j+1][l+1] %= 998244353
                dp[i+1][j][l+1] += dp[i][j][l] * (m-j)
                dp[i+1][j][l+1] %= 998244353
    return dp[n][m][k]

if __name__ == '__main__':
    solve()