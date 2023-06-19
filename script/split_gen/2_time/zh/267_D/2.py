def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + a[i] * (j + 1))
            if j + 1 < m:
                dp[i + 2][j + 2] = max(dp[i + 2][j + 2], dp[i][j] + a[i] * (j + 1) + a[i + 1] * (j + 2))
    print(dp[n][m])
solve()
