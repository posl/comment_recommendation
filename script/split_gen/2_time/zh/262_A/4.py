def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    c = []
    y = []
    for i in range(m):
        ci, yi = map(int, input().split())
        c.append(ci)
        y.append(yi)
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(n):
        for j in range(i + 1):
            if j == 0:
                dp[i + 1][j] = dp[i][j] + x[i]
            else:
                dp[i + 1][j] = max(dp[i][j] + x[i], dp[i][j - 1])
    ans = 0
    for i in range(m):
        for j in range(n + 1):
            ans = max(ans, dp[c[i]][j] + y[i])
    print(ans)
