def solve():
    mod = 998244353
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    dp = [[0 for i in range(3001)] for j in range(n)]
    for i in range(a[0], b[0] + 1):
        dp[0][i] = 1
    for i in range(1, n):
        for j in range(3001):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
            if j > b[i]:
                dp[i][j] -= dp[i - 1][j - b[i] - 1]
            if j - a[i] - 1 >= 0:
                dp[i][j] -= dp[i - 1][j - a[i] - 1]
            dp[i][j] %= mod
    print(dp[n - 1][3000])
