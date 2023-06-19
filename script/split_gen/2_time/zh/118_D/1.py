def solve(N, M, A):
    # dp[i]表示用i根火柴棍所能形成的最大整数
    dp = [-1] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):
        for j in range(M):
            if i >= A[j] and dp[i - A[j]] != -1:
                dp[i] = max(dp[i], dp[i - A[j]] * 10 + j + 1)
    return dp[N]
