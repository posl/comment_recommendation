def solve(x, y):
    dp = [[0 for _ in range(y+1)] for _ in range(x+1)]
    dp[0][0] = 1
    for i in range(x+1):
        for j in range(y+1):
            if i >= 1 and j >= 2:
                dp[i][j] += dp[i-1][j-2]
            if i >= 2 and j >= 1:
                dp[i][j] += dp[i-2][j-1]
            dp[i][j] %= 1000000007
    return dp[x][y]
