def main():
    n = int(input())
    x, y = map(int, input().split())
    a = []
    b = []
    for _ in range(n):
        a_, b_ = map(int, input().split())
        a.append(a_)
        b.append(b_)
    dp = [[[0] * (x + 1) for _ in range(y + 1)] for _ in range(n + 1)]
    for i in range(n):
        for j in range(y + 1):
            for k in range(x + 1):
                if j - b[i] >= 0 and k - a[i] >= 0:
                    dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j - b[i]][k - a[i]] + 1)
                dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j][k])
    if dp[n][y][x] == 0:
        print(-1)
    else:
        print(dp[n][y][x])
