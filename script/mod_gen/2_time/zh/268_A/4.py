def max_sum_subsequence(N, M, A):
    # dp[i][j]表示前i个数中取j个数的最大值
    dp = [[0 for i in range(M + 1)] for j in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if j > i:
                continue
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + A[i - 1] * j)
    return dp[N][M]

if __name__ == '__main__':
    max_sum_subsequence()