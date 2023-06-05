def solve(n, m, x):
    if n == 1:
        return 0
    x.sort()
    if n == 2:
        return x[1] - x[0]
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = x[1] - x[0]
    dp[2] = x[2] - x[0]
    for i in range(3, n+1):
        dp[i] = min(dp[i-1] + x[i-1] - x[i-2], dp[i-2] + x[i-1] - x[i-3])
    return dp[n]
