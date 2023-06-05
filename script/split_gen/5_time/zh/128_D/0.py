def solve(n, k, v):
    dp = [[[0 for i in range(n+1)] for j in range(n+1)] for l in range(k+1)]
    for i in range(1, k+1):
        for j in range(n+1):
            for l in range(n+1):
                if j > 0:
                    dp[i][j][l] = max(dp[i][j][l], dp[i-1][j-1][l]+v[j-1])
                if l > 0:
                    dp[i][j][l] = max(dp[i][j][l], dp[i-1][j][l-1])
                if j > 0 and l > 0:
                    dp[i][j][l] = max(dp[i][j][l], dp[i-1][j-1][l-1])
    return dp[k][n][n]
