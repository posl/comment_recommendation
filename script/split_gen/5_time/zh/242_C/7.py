def solve(n):
    dp = [[0 for i in range(10)] for j in range(n)]
    for i in range(1, 10):
        dp[0][i] = 1
    for i in range(n-1):
        for j in range(10):
            if j - 1 >= 0:
                dp[i+1][j-1] += dp[i][j]
            if j + 1 <= 9:
                dp[i+1][j+1] += dp[i][j]
    ans = 0
    for i in range(10):
        ans += dp[n-1][i]
    return ans % 998244353
