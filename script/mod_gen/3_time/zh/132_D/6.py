def problems132_d():
    n,k = map(int,input().split())
    mod = 10**9+7
    #dp[i][j]表示i个球，j步走完的方案数
    dp = [[0]*(k+1) for i in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(k):
            dp[i+1][j+1] += dp[i][j+1]
            dp[i+1][j+1] %= mod
            dp[i+1][j] += dp[i][j]*(n-k-i+j+1)
            dp[i+1][j] %= mod
    print(dp[n][k])

if __name__ == '__main__':
    problems132_d()