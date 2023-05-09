def knapsack(N, W, V, X):
    dp = [[0]*(X+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(X+1):
            if j < W[i]:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = max(dp[i][j], dp[i][j-W[i]]+V[i])
    return dp[N][X]

if __name__ == '__main__':
    knapsack()