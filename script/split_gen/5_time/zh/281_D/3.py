def solve(n, k, d, a):
    dp = [[[0 for i in range(10001)] for j in range(101)] for k in range(101)]
    dp[0][0][0] = 1
    for i in range(n):
        for j in range(k):
            for k in range(d):
                dp[i + 1][j][k] += dp[i][j][k]
                dp[i + 1][j + 1][(k + a[i]) % d] += dp[i][j][k]
    if dp[n][k][0] == 0:
        return -1
    else:
        return dp[n][k][0] - 1
