def solve():
    N = int(input())
    mod = 998244353
    dp = [[0 for i in range(9)] for j in range(N+1)]
    for i in range(9):
        dp[1][i] = 1
    for i in range(2,N+1):
        dp[i][0] = dp[i-1][0] + dp[i-1][1]
        dp[i][8] = dp[i-1][7] + dp[i-1][8]
        for j in range(1,8):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]
    ans = 0
    for i in range(1,9):
        ans += dp[N][i]
    print(ans%mod)
