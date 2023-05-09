def main():
    N, K = map(int, input().split())
    MOD = 10 ** 9 + 7
    dp = [[0] * (N + 1) for _ in range(K + 1)]
    dp[0][0] = 1
    for i in range(1, K + 1):
        for j in range(1, N + 1):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
            dp[i][j] %= MOD
    for i in range(1, K + 1):
        print(dp[i][N] * dp[K - 1][N - 1] % MOD)
main()

if __name__ == '__main__':
    main()