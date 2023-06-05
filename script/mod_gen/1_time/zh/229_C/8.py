def solve(N, W, A, B):
    dp = [[0 for j in range(W+1)] for i in range(N+1)]
    for i in range(1, N+1):
        for j in range(W+1):
            if j < B[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-B[i-1]] + A[i-1])
    return dp[N][W]

if __name__ == '__main__':
    solve()