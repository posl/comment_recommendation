def main():
    n,m = map(int, input().split())
    x = list(map(int, input().split()))
    c = []
    y = []
    for i in range(m):
        c_, y_ = map(int, input().split())
        c.append(c_)
        y.append(y_)
    c_y = sorted(zip(c, y), key=lambda x: x[0])
    c = [x[0] for x in c_y]
    y = [x[1] for x in c_y]
    dp = [[-float("inf") for _ in range(n+1)] for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(n):
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+x[i])
            if j+1 in c:
                dp[i+1][1] = max(dp[i+1][1], dp[i][j]+y[c.index(j+1)])
    print(max(dp[n]))
