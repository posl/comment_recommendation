def solve(n, m, a):
    # dp[i][j] := i番目までの数列からj個選んだ時の最大値
    dp = [[-float('inf')]*(m+1) for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(m+1):
            if j > 0:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j-1] + (i+1)*a[i])
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
    return dp[n][m]
