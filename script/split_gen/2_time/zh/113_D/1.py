def solve(h,w,k):
    #dp[i][j]表示第i行，第j个位置的方案数
    #dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    dp = [[0 for i in range(w+2)] for j in range(h+1)]
    dp[0][k] = 1
    mod = 10**9 + 7
    for i in range(1,h+1):
        for j in range(1,w+1):
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % mod
    return dp[h][1]
h,w,k = map(int,input().split())
print(solve(h,w,k))
