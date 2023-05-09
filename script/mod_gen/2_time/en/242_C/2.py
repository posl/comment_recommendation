def main():
    N = int(input())
    mod = 998244353
    dp = [[0] * 10 for _ in range(N)]
    for i in range(1, 10):
        dp[0][i] = 1
    for i in range(1, N):
        dp[i][0] = dp[i - 1][1]
        for j in range(1, 9):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
        dp[i][9] = dp[i - 1][8]
    print(sum(dp[-1]) % mod)

if __name__ == '__main__':
    main()