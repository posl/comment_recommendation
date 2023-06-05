def get_min_swap_times(s):
    target = "atcoder"
    s_len = len(s)
    target_len = len(target)
    dp = [[0 for _ in range(s_len + 1)] for _ in range(target_len + 1)]
    for i in range(1, target_len + 1):
        dp[i][0] = dp[i - 1][0] + i
    for j in range(1, s_len + 1):
        dp[0][j] = dp[0][j - 1] + 1
    for i in range(1, target_len + 1):
        for j in range(1, s_len + 1):
            if target[i - 1] == s[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i][j - 1] + 1, dp[i - 1][j] + i)
    return dp[target_len][s_len]
