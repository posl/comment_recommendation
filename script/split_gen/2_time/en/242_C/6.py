def solve(n):
    if n == 1:
        return 10
    dp = [[0] * 2 for _ in range(10)]
    for i in range(1, 10):
        dp[i][0] = 1
    for i in range(1, n):
        for j in range(10):
            if j == 0:
                dp[j][1] = dp[j + 1][0]
            elif j == 9:
                dp[j][1] = dp[j - 1][0]
            else:
                dp[j][1] = dp[j - 1][0] + dp[j + 1][0]
            dp[j][0] = dp[j][1]
    return sum(dp[i][0] for i in range(10)) % 998244353
