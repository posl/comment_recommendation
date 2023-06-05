def func(s):
    dp = [0]*(s+1)
    dp[0] = 1
    for i in range(3, s+1):
        dp[i] = (dp[i-1] + dp[i-3]) % (10**9+7)
    return dp[s]

if __name__ == '__main__':
    func()