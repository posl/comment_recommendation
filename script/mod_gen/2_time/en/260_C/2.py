def solve():
    N, X, Y = map(int, input().split())
    dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
    dp[1][0] = 1
    for i in range(1, N):
        for j in range(N):
            dp[i+1][j] += dp[i][j] * (i - j)
            dp[i+1][j+1] += dp[i][j] * (j + 1)
            dp[i+1][j+1] += dp[i][j] * (i - j)
            dp[i+1][j] += dp[i][j] * (j + 1)
        dp[i+1][N] += dp[i][N] * (i - N)
        dp[i+1][N] += dp[i][N] * (N + 1)
        dp[i+1][N-1] += dp[i][N] * (N + 1)
    print(dp[N][N-1] * X + dp[N][N] * Y)

if __name__ == '__main__':
    solve()