def calc(N, M, A):
    MOD = 10**9 + 7
    dp = [0] * (N+1)
    dp[0] = 1
    for i in range(1, N+1):
        if i in A:
            dp[i] = 0
        else:
            dp[i] = dp[i-1] + dp[i-2]
            dp[i] %= MOD
    return dp[N]
