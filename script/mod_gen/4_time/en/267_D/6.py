def solve(N, M, A):
    A.sort(reverse=True)
    dp = [[0 for i in range(M+1)] for j in range(N+1)]
    for i in range(N):
        for j in range(M):
            dp[i+1][j+1] = max(dp[i][j+1], dp[i][j] + (i+1)*A[i])
    return dp[N][M]
N, M = map(int, input().split())
A = list(map(int, input().split()))
print(solve(N, M, A))
