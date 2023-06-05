def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = []
    Y = []
    for i in range(M):
        c, y = map(int, input().split())
        C.append(c)
        Y.append(y)
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        for j in range(N + 1):
            if i > 0 and j > 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + Y[i - 1])
            if i > 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j])
            if j > 0:
                dp[i][j] = max(dp[i][j], dp[i][j - 1])
            if i == j:
                dp[i][j] = max(dp[i][j], dp[i][j - 1] + X[i - 1])
    print(dp[N][N])

if __name__ == '__main__':
    main()