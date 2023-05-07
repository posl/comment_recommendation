def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    c = []
    y = []
    for i in range(m):
        c1, y1 = map(int, input().split())
        c.append(c1)
        y.append(y1)
    dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
    for i in range(n):
        for j in range(n + 1):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + x[i])
            if j in c:
                dp[i + 1][0] = max(dp[i + 1][0], dp[i][j] + y[c.index(j)])
    print(max(dp[n]))
