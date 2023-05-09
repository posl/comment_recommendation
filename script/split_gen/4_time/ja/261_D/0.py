def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    c = [0] * m
    y = [0] * m
    for i in range(m):
        c[i], y[i] = map(int, input().split())
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        dp[i + 1][0] = dp[i][0] + x[i]
        dp[i + 1][1] = max(dp[i][0], dp[i][1]) + x[i]
        for j in range(2, i + 2):
            dp[i + 1][j] = max(dp[i][j - 1] + x[i], dp[i][j])
    ans = 0
    for i in range(m):
        for j in range(1, n + 1):
            ans = max(ans, dp[n][j] + (n - j) // c[i] * y[i])
    print(ans)
