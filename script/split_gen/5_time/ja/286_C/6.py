def solve(n,a,b,s):
    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n):
        dp[i][i] = 0
    for i in range(n-1):
        dp[i][i+1] = 0
        if s[i] == s[i+1]:
            dp[i][i+1] = 0
        else:
            dp[i][i+1] = a
    for i in range(2,n):
        for j in range(n-i):
            if s[j] == s[j+i]:
                dp[j][j+i] = dp[j+1][j+i-1]
            else:
                dp[j][j+i] = min(dp[j+1][j+i]+a,dp[j][j+i-1]+a,b+dp[j+1][j+i-1])
    return dp[0][n-1]
