def max_sum(a, m):
    n = len(a)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(m + 1):
            if j == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i - 1][j]
                if i >= j:
                    dp[i][j] = max(dp[i][j], dp[i - j][j - 1] + j * a[i - 1])
    return dp[n][m]
n, m = map(int, input().split())
a = list(map(int, input().split()))
print(max_sum(a, m))
