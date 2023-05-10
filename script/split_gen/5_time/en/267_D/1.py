def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    dp = [[0] * (N + 1) for _ in range(M + 1)]
    for i in range(M):
        for j in range(N):
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i + 1][j], dp[i][j] + (i + 1) * A[j])
    print(dp[M][N])
