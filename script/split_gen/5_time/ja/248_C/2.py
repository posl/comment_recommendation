def main():
    n,m,k = map(int,input().split())
    mod = 998244353
    dp = [[[0 for i in range(k+1)] for j in range(m+1)] for l in range(n+1)]
    dp[0][0][0] = 1
    for i in range(n):
        for j in range(m+1):
            for l in range(k+1):
                if dp[i][j][l] == 0:
                    continue
                dp[i+1][j][l] += dp[i][j][l]
                dp[i+1][j][l] %= mod
                if l+j <= k:
                    dp[i+1][j][l+j] += dp[i][j][l]
                    dp[i+1][j][l+j] %= mod
                if j+1 <= m:
                    dp[i+1][j+1][l] += dp[i][j][l]
                    dp[i+1][j+1][l] %= mod
    print(dp[n][m][k])
