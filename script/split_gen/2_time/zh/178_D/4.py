def solve(n):
    dp = [0 for i in range(2001)]
    dp[0] = 1
    for i in range(3,n+1):
        for j in range(i,2001):
            dp[j] += dp[j-i]
            dp[j] %= 1000000007
    return dp[n]
n = int(input())
print(solve(n))
