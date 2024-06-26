def max_sum(n, m, a):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, min(i+1, m+1)):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + i*a[i-1])
    return dp[n][m]
n, m = map(int, input().split())
a = list(map(int, input().split()))
print(max_sum(n, m, a))
