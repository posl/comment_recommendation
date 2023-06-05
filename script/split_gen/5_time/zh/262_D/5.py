def solve(n,a):
    #dp[i][j]表示前i个数中选j个数，这j个数的平均值是整数的情况数
    dp = [[0 for i in range(n+1)] for j in range(n+1)]
    dp[0][0] = 1
    for i in range(1,n+1):
        for j in range(n+1):
            dp[i][j] = dp[i-1][j]
            if j-1 >= 0 and a[i-1] % j == 0:
                dp[i][j] += dp[i-1][j-1]
    res = 0
    for i in range(1,n+1):
        res += dp[n][i]
    return res
