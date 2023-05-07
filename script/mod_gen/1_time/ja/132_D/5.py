def main():
    N, K = map(int, input().split())
    MOD = 10 ** 9 + 7
    # dp[i][j]: 青いボールが i 個、赤いボールが j 個あるときの並べ方の総数
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N + 1):
        for j in range(N + 1):
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
            dp[i][j] %= MOD
    for i in range(1, K + 1):
        ans = dp[i][N - i] * dp[K - i][N - K]
        ans %= MOD
        print(ans)

if __name__ == '__main__':
    main()