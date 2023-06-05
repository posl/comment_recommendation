def solve(S):
    dp = [0]*(S+1)
    dp[0] = 1
    for i in range(3,S+1):
        for j in range(i-2):
            dp[i] += dp[j]
            dp[i] %= 1000000007
    return dp[S]
