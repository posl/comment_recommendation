def solve():
    # 状态转移方程
    # dp[i] = sum(dp[i - L[j]] for j in range(k) if L[j] <= i <= R[j])
    # dp[i] = dp[i - 2] + dp[i - 3] + dp[i - 4] + dp[i - 5] + dp[i - 6]
    # dp[i] = dp[i - 3] + dp[i - 5] + dp[i - 6] + dp[i - 7] + dp[i - 8]
    # dp[i] = dp[i - 5] + dp[i - 6] + dp[i - 7] + dp[i - 8] + dp[i - 9] + dp[i - 10]
    # dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4] + dp[i - 5] + dp[i - 6]
    # dp[i] = dp[i - 1] + dp[i - 3] + dp[i - 5] + dp[i - 6] + dp[i - 7] + dp[i - 8]
    # dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 5] + dp[i - 6] + dp[i - 7]
    # dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4] + dp[i - 5] + dp[i - 6]
    # dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4] + dp[i - 5] + dp[i - 6]
    # dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4] + dp[i - 5] + dp[i - 6]
    # dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4] + dp[i - 5] + dp[i - 6]
    # dp[i
