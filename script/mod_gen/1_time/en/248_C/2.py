def main():
    n, m, k = map(int, input().split())
    dp = [[[0 for _ in range(k+1)] for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            for l in range(1, k+1):
                if i == 1 and j <= l:
                    dp[i][j][l] = 1
                elif i >= 2 and j <= l:
                    dp[i][j][l] = dp[i-1][j][l] + dp[i][j][l-j]
    print(dp[n][m][k] % 998244353)

if __name__ == '__main__':
    main()