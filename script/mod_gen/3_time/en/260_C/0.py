def solve():
    N, X, Y = map(int, input().split())
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][1] = 1
    for i in range(N):
        for j in range(N - i + 1):
            dp[i + j][j] += dp[i][j] * (i + j)
            dp[i + j - 1][j + 1] += dp[i][j] * j
            dp[i + j - 1][j] += dp[i][j] * (i + 1)
    print(dp[N][1] * X + dp[N][0] * Y)
solve()

if __name__ == '__main__':
    solve()