def solve(n, m, a):
    dp = [[-float('inf') for i in range(m + 1)] for j in range(n + 1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(m + 1):
            if j - 1 >= 0:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - 1] + (i + 1) * a[i])
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
    return dp[n][m]
n, m = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, m, a))
