def solve(n, m, x, c, y):
    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j+1])
            dp[i+1][min(j+c[i], n)] = max(dp[i+1][min(j+c[i], n)], dp[i][j+1] + y[i])
        dp[i+1][0] = max(dp[i+1][0], dp[i][0] + x[i])
    return max(dp[n])
n, m = map(int, input().split())
x = list(map(int, input().split()))
c = []
y = []
for _ in range(m):
    c_, y_ = map(int, input().split())
    c.append(c_)
    y.append(y_)
print(solve(n, m, x, c, y))
