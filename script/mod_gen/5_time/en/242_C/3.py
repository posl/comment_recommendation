def main():
    N = int(input())
    dp = [[0] * 10 for _ in range(N)]
    dp[0] = [1] * 10
    for i in range(1, N):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j + 1]
            elif j == 9:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] + dp[i - 1][j + 1]
    print(sum(dp[N - 1]) % 998244353)

if __name__ == '__main__':
    main()