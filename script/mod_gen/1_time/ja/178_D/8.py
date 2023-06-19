def dp(s):
    dp = [0 for i in range(s+1)]
    dp[0] = 1
    for i in range(3,s+1):
        for j in range(3,i+1):
            dp[i] += dp[i-j]
    return dp[s]
S = int(input())
print(dp(S)%(10**9+7))
