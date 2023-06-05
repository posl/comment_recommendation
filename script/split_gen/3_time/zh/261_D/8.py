def main():
    n,m = map(int, input().split())
    x = list(map(int, input().split()))
    c = []
    y = []
    for _ in range(m):
        c_i, y_i = map(int, input().split())
        c.append(c_i)
        y.append(y_i)
    dp = [[-float('inf')]*(n+1) for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(n):
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + x[i])
        for j in range(n):
            dp[i+1][0] = max(dp[i+1][0], dp[i][j] + y[j])
    print(max(dp[n]))
