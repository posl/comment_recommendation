def func(h,w,k):
    dp = [[0 for _ in range(w)] for _ in range(h+1)]
    dp[0][0] = 1
    for i in range(h):
        for j in range(w):
            dp[i+1][j] += dp[i][j]
            dp[i+1][j] %= 1000000007
            if j >= 1:
                dp[i+1][j-1] += dp[i][j]
                dp[i+1][j-1] %= 1000000007
            if j < w-1:
                dp[i+1][j+1] += dp[i][j]
                dp[i+1][j+1] %= 1000000007
    return dp[h][k-1]
h,w,k = map(int,input().split())
print(func(h,w,k))
