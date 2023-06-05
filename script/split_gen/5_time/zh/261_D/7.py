def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    c = []
    y = []
    for i in range(m):
        c_i, y_i = map(int, input().split())
        c.append(c_i)
        y.append(y_i)
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n):
        for j in range(i+1):
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+x[i])
            if j+1 in c:
                dp[i+1][1] = max(dp[i+1][1], dp[i][j]+y[c.index(j+1)])
    print(max(dp[n]))
