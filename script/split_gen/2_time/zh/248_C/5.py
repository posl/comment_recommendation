def main():
    n, m, k = map(int, input().split())
    dp = [[[0 for i in range(k + 1)] for j in range(m + 1)] for k in range(n + 1)]
    dp[0][0][0] = 1
    for i in range(n):
        for j in range(m + 1):
            for l in range(k + 1):
                dp[i + 1][j][l] += dp[i][j][l]
                dp[i + 1][j][l] %= 998244353
                if j < m and l + j + 1 <= k:
                    dp[i + 1][j + 1][l + j + 1] += dp[i][j][l]
                    dp[i + 1][j + 1][l + j + 1] %= 998244353
    print(dp[n][m][k])
