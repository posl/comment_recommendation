def max_value(N, V, C):
    # 递归
    # if N == 0:
    #     return 0
    # elif V[N-1] < C[N-1]:
    #     return max_value(N-1, V, C)
    # else:
    #     return max(max_value(N-1, V, C), max_value(N-1, V, C))
    # 动态规划
    dp = [[0 for i in range(1000)] for j in range(1000)]
    for i in range(N):
        for j in range(1000):
            if j < C[i]:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = max(dp[i][j], dp[i][j-C[i]]+V[i])
    return dp[N][999]
