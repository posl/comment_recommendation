def solve(L):
    dp = [0] * (L+1)
    dp[0] = 1
    for i in range(1,L+1):
        dp[i] = dp[i-1]
        if i >= 2:
            dp[i] += dp[i-2]
        if i >= 4:
            dp[i] += dp[i-4]
        if i >= 7:
            dp[i] += dp[i-7]
    return dp[L]
print(solve(int(input())))
