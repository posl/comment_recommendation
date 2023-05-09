def solve():
    n, w = map(int, input().split())
    a, b = [], []
    for i in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    dp = [[0 for i in range(w + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(w + 1):
            if j - b[i - 1] >= 0:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - b[i - 1]] + a[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]
    print(dp[n][w])
