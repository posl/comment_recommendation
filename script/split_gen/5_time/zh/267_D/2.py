def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(M):
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i][j] + (i + 1) * A[i])
    print(dp[N][M])
