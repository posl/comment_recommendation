def solve(N, K, LR):
    MOD = 998244353
    dp = [0] * (N + 1)
    dp[1] = 1
    for i in range(1, N):
        for l, r in LR:
            dp[i + l] += dp[i]
            dp[i + l] %= MOD
            dp[i + r + 1] -= dp[i]
            dp[i + r + 1] %= MOD
    return dp[N]
