def main():
    n, m, k = map(int, input().split())
    dp = [[[0 for _ in range(k+1)] for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1, m+1):
        dp[1][i][i] = 1
    for i in range(2, n+1):
        for j in range(1, m+1):
            for s in range(1, k+1):
                if s - j > 0:
                    dp[i][j][s] = dp[i][j-1][s] + dp[i-1][j-1][s-j]
                else:
                    dp[i][j][s] = dp[i][j-1][s]
    print(dp[n][m][k]%998244353)

if __name__ == '__main__':
    main()