def main():
    n,m,k = map(int, input().split())
    mod = 998244353
    dp = [[[0]*(k+1) for _ in range(m+1)] for _ in range(n+1)]
    dp[0][0][0] = 1
    for i in range(n):
        for j in range(m+1):
            for l in range(k+1):
                dp[i+1][j][l] += dp[i][j][l]
                dp[i+1][j][l] %= mod
                if j < m and l+i+1 <= k:
                    dp[i+1][j+1][l+i+1] += dp[i][j][l]
                    dp[i+1][j+1][l+i+1] %= mod
    print(dp[n][m][k])
