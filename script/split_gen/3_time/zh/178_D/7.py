def solve(s):
    if s < 3:
        return 0
    dp = [[0 for _ in range(s + 1)] for _ in range(s + 1)]
    dp[0][0] = 1
    for i in range(3, s + 1):
        for j in range(s + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= i:
                dp[i][j] += dp[i][j - i]
            dp[i][j] %= 1000000007
    return dp[s][s]
