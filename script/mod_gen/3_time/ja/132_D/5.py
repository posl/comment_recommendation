def main():
    N, K = list(map(int, input().split()))
    MOD = 10**9 + 7
    # dp[i][j]: i個のボールからj個の青いボールを選ぶ場合の数
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        dp[i][0] = 1
    for i in range(1, N + 1):
        for j in range(1, K + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            dp[i][j] %= MOD
    # dp2[i]: i個のボールからi個の青いボールを選ぶ場合の数
    dp2 = [0] * (N + 1)
    for i in range(1, N + 1):
        dp2[i] = dp[i][i]
    # dp3[i]: i個のボールからi個の青いボールを選ぶ場合の数の累積和
    dp3 = [0] * (N + 1)
    for i in range(1, N + 1):
        dp3[i] = (dp3[i - 1] + dp2[i]) % MOD
    # dp4[i]: i個のボールからi個の青いボールを選ぶ場合の数の累積和の累積和
    dp4 = [0] * (N + 1)
    for i in range(1, N + 1):
        dp4[i] = (dp4[i - 1] + dp3[i]) % MOD
    for i in range(1, K + 1):
        print(dp4[i])

if __name__ == '__main__':
    main()