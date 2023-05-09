def solve(n, m, a):
    cnt = [0] * m
    for i in a:
        cnt[i] += 1
    if cnt[0] > 0:
        return 1
    dp = [0] * m
    dp[0] = 1
    for i in range(1, m):
        if cnt[i] > 0:
            dp[i] = 1
        else:
            dp[i] = dp[i - 1] + dp[i - 2]
    return dp[-1]
