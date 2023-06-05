def solve(N, K, V):
    # dp[i][j][k]表示第i次操作后，左端有j个宝石，右端有k个宝石时的最大值
    dp = [[[0 for k in range(N+1)] for j in range(N+1)] for i in range(K+1)]
    for i in range(N):
        dp[0][0][i] = V[i]
    for i in range(1, K+1):
        for j in range(N+1):
            for k in range(N+1):
                if j > 0:
                    dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-1][k]+V[j-1])
                if k > 0:
                    dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k-1]+V[N-k])
                if j < N:
                    dp[i][j][k] = max(dp[i][j][k], dp[i-1][j+1][k])
                if k < N:
                    dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k+1])
    return dp[K][0][0]
