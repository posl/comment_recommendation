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
    for i in range(N):
        for j in range(N + 1):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            if j < N:
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + X[i])
        for k in range(M):
            if j >= C[k]:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - C[k]] + Y[k])
    print(max(dp[N]))

if __name__ == '__main__':
    main()