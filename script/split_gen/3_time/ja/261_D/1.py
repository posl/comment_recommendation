def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = [0] * M
    Y = [0] * M
    for i in range(M):
        C[i], Y[i] = map(int, input().split())
    dp = [[0] * (N + 1) for i in range(N + 1)]
    for i in range(N):
        for j in range(N):
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + X[i])
            if j + 1 >= C[0]:
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j + 1 - C[0]] + Y[0])
        for j in range(1, M):
            for k in range(N):
                if k + 1 >= C[j]:
                    dp[i + 1][k + 1] = max(dp[i + 1][k + 1], dp[i][k + 1 - C[j]] + Y[j])
    print(max(dp[N]))
