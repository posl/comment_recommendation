def main():
    n, m, k = map(int, input().split())
    dp = [[[0 for _ in range(k+1)] for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1, m+1):
        dp[1][i][i] = 1
    for i in range(2, n+1):
        for j in range(1, m+1):
            for l in range(1, k+1):
                if l - j >= 0:
                    dp[i][j][l] = (dp[i][j-1][l] + dp[i-1][j][l-j]) % 998244353
                else:
                    dp[i][j][l] = dp[i][j-1][l]
    print(dp[n][m][k])

if __name__ == '__main__':
    main()