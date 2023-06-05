def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    c = []
    y = []
    for i in range(m):
        c_i, y_i = map(int, input().split())
        c.append(c_i)
        y.append(y_i)
    dp = [[0] * (n + 1) for _ in range(n + 1)] # dp[i][j]表示第i次投掷硬币后，连续j次正面朝上时的最大金额
    for i in range(n):
        for j in range(n):
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j + 1] + x[i])
            if j + 1 in c:
                dp[i + 1][1] = max(dp[i + 1][1], dp[i][j + 1] + y[c.index(j + 1)])
    print(max(dp[-1]))
