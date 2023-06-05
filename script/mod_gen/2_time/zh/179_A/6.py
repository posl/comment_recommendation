def solve(s):
    mod = 10**9+7
    dp = [[0 for i in range(s+1)] for j in range(s+1)]
    for i in range(3,s+1):
        dp[1][i] = 1
    for i in range(2,s+1):
        for j in range(3,s+1):
            if i>j:
                dp[i][j] = dp[i-1][j]*i%mod
            else:
                dp[i][j] = (dp[i-1][j]*i+dp[i][j-i])%mod
    return dp[s][s]
s = int(input())
print(solve(s))
