def largest_integer(n,m,a):
    dp = [-1]*(n+1)
    dp[0] = 0
    for i in range(1,n+1):
        for j in range(m):
            if i >= a[j] and dp[i-a[j]] >= 0:
                dp[i] = max(dp[i], dp[i-a[j]]*10+j+1)
    return dp[n]
