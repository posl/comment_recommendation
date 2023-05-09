def solve(n,k,lr):
    mod = 998244353
    dp = [0 for i in range(n)]
    dp[0] = 1
    for i in range(n):
        for j in range(k):
            if i+lr[j][0] < n:
                dp[i+lr[j][0]] += dp[i]
                dp[i+lr[j][0]] %= mod
            if i+lr[j][1]+1 < n:
                dp[i+lr[j][1]+1] -= dp[i]
                dp[i+lr[j][1]+1] %= mod
    return dp[n-1]
