def solve(n, m, k):
    mod = 998244353
    dp = [[[0 for _ in range(k+1)] for _ in range(m+1)] for _ in range(n+1)]
    dp[0][0][0] = 1
    for i in range(n):
        for j in range(m+1):
            for l in range(k+1):
                if l+j <= k:
                    dp[i+1][j][l+j] = (dp[i+1][j][l+j] + dp[i][j][l]) % mod
                if j+1 <= m and l+j+1 <= k:
                    dp[i+1][j+1][l+j+1] = (dp[i+1][j+1][l+j+1] + dp[i][j][l]) % mod
    return dp[n][m][k]

if __name__ == '__main__':
    solve()