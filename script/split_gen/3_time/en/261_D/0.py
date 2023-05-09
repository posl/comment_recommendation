def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = [0] * M
    Y = [0] * M
    for i in range(M):
        C[i], Y[i] = map(int, input().split())
    # dp[i][j] = i番目までのコインを投げた時、連続でj回コインが表が出た時の最大値
    # dp[i][j] = max(dp[i-1][j], dp[i-C[j]][j-1] + X[i] + Y[j])
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i - C[j - 1]][j - 1] + X[i - 1] + Y[j - 1])
    print(dp[N][N])
