def main():
    H, W, K = map(int, input().split())
    MOD = 10 ** 9 + 7
    dp = [[0] * (W + 1) for _ in range(H + 1)]
    dp[0][1] = 1
    for i in range(H):
        for j in range(1, W + 1):
            dp[i + 1][j] += dp[i][j] * fib(j - 1) * fib(W - j) % MOD
            dp[i + 1][j] += dp[i][j - 1] * fib(j - 2) * fib(W - j) % MOD
            dp[i + 1][j] += dp[i][j + 1] * fib(j - 1) * fib(W - j - 1) % MOD
            dp[i + 1][j] %= MOD
    print(dp[H][K])

if __name__ == '__main__':
    main()