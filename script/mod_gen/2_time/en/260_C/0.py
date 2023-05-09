def main():
    N, X, Y = map(int, input().split())
    dp = [[0] * (N+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(N):
            dp[i+1][j] += dp[i][j] * (i / (i + j + 1))
            dp[i][j+1] += dp[i][j] * (j / (i + j + 1))
    ans = 0
    for i in range(N):
        ans += dp[i][N-i-1] * X
        ans += dp[i][N-i] * Y
    print(int(ans))

if __name__ == '__main__':
    main()