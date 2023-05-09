def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = [0] * M
    Y = [0] * M
    for i in range(M):
        C[i], Y[i] = map(int, input().split())
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(N):
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j])
            dp[i + 1][0] = max(dp[i + 1][0], dp[i][j] + X[i])
            for k in range(M):
                if j == C[k] - 1:
                    dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + Y[k])
    print(max(dp[N]))
