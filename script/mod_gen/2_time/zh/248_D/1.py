def solve(n,m,k):
    MOD = 998244353
    dp = [[[0 for _ in range(k+1)] for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1,m+1):
        dp[1][i][i] = 1
    for i in range(1,n):
        for j in range(1,m+1):
            for l in range(1,k+1):
                if l+j <= k:
                    dp[i+1][j][l+j] = (dp[i+1][j][l+j] + dp[i][j][l]) % MOD
                dp[i+1][j][l] = (dp[i+1][j][l] + dp[i][j][l]) % MOD
                if j < m and l+j <= k:
                    dp[i+1][j+1][l+j] = (dp[i+1][j+1][l+j] + dp[i][j][l]) % MOD
    ans = 0
    for i in range(1,m+1):
        ans = (ans + dp[n][i][k]) % MOD
    return ans

if __name__ == '__main__':
    solve()