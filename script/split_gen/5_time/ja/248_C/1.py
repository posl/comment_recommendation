def main():
    n,m,k = map(int,input().split())
    mod = 998244353
    dp = [[[0 for _ in range(k+1)] for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i == 1:
                if j <= k:
                    dp[i][j][j] = 1
            else:
                for l in range(1,k+1):
                    dp[i][j][l] = dp[i][j-1][l]
                    if l-j >= 0:
                        dp[i][j][l] += dp[i-1][j][l-j]
                    dp[i][j][l] %= mod
    print(dp[n][m][k])
