def solve(n, l, r, a):
    dp = [[0, 0] for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][0] = min(dp[i - 1][0] + l * a[i - 1], dp[i - 1][1] + l * a[i - 1])
        dp[i][1] = min(dp[i - 1][0] + r * a[i - 1], dp[i - 1][1] + r * a[i - 1])
    return min(dp[n][0], dp[n][1])
