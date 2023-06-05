def problems132_d():
    n,k = map(int,input().split())
    mod = 10**9+7
    dp = [[0 for i in range(n+1)] for j in range(k+1)]
    dp[0][0] = 1
    for i in range(1,k+1):
        for j in range(n+1):
            if j-i >= 0:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1])%mod
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[k][n])
