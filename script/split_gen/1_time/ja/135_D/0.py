def solve(s):
    dp = [[0 for _ in range(13)] for _ in range(len(s)+1)]
    dp[0][0] = 1
    for i in range(len(s)):
        for j in range(13):
            if s[i] == "?":
                for k in range(10):
                    dp[i+1][(j*10+k)%13] += dp[i][j]
            else:
                dp[i+1][(j*10+int(s[i]))%13] += dp[i][j]
        for j in range(13):
            dp[i+1][j] %= 10**9+7
    return dp[len(s)][5]
