def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A
    dp = [[0] * (N + 1) for _ in range(M + 1)]
    for i in range(1, M + 1):
        for j in range(i, N + 1):
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - 1] + i * A[j])
    print(dp[M][N])
