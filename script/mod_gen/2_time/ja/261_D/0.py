def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = [0] * M
    Y = [0] * M
    for i in range(M):
        C[i], Y[i] = map(int, input().split())
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(N + 1):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            if X[i] == 1:
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + Y[j])
    print(dp[N][N])

if __name__ == '__main__':
    main()