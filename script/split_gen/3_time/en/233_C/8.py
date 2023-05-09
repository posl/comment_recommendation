def main():
    n, x = map(int, input().split())
    l = [list(map(int, input().split())) for i in range(n)]
    l = [[0, 0]] + l
    dp = [[0] * (x + 1) for i in range(n + 1)]
    dp[0][1] = 1
    for i in range(1, n + 1):
        for j in range(x + 1):
            for k in range(l[i][0]):
                if j * l[i][k + 1] <= x:
                    dp[i][j * l[i][k + 1]] += dp[i - 1][j]
    print(dp[n][x])
