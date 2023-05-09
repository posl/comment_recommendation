def solve(N, K):
    MOD = 10**9 + 7
    # dp[i][j] := i個のボールでj個の青いボールを選ぶ方法の数
    dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        for j in range(i + 1):
            dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1] * (i - 1)) % MOD
    for i in range(1, K + 1):
        print(dp[N][i] * dp[N - 1][i - 1] % MOD)

if __name__ == '__main__':
    solve()