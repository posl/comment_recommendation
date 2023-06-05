def dp(N,M,X,C,A):
    dp = [[float('inf') for _ in range(X+1)] for _ in range(M+1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(M-1,-1,-1):
            for k in range(X+1):
                if k >= C[i]:
                    dp[j+1][k] = min(dp[j+1][k],dp[j][k-C[i]]+A[i])
    return dp[M][X] if dp[M][X] != float('inf') else -1
