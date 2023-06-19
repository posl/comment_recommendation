def max_sum(n, m, a):
    dp = [[-float('inf') for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, min(m+1, i+1)):
            if j == 1:
                dp[i][j] = max(dp[i-1][j], 0) + a[i-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + j * a[i-1]
    return max(dp[-1])

if __name__ == '__main__':
    max_sum()