def solve():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    c = []
    y = []
    for _ in range(m):
        c_, y_ = map(int, input().split())
        c.append(c_)
        y.append(y_)
    dp = [[-10**18]*(n+1) for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(n):
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + x[i])
            for k in range(m):
                if j+1 == c[k]:
                    dp[i+1][0] = max(dp[i+1][0], dp[i][j] + y[k])
    print(max(dp[-1]))

if __name__ == '__main__':
    solve()