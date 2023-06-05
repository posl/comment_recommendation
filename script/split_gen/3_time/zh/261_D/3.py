def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    c = []
    y = []
    for i in range(m):
        c_temp, y_temp = map(int, input().split())
        c.append(c_temp)
        y.append(y_temp)
    dp = [[-float('inf')] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(n):
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + x[i])
            for k in range(m):
                if j + 1 == c[k]:
                    dp[i + 1][0] = max(dp[i + 1][0], dp[i + 1][j + 1] + y[k])
    print(max(dp[n]))
