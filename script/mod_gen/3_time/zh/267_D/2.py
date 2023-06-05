def max_sum(a, n, m):
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if j > i:
                dp[i][j] = -1000000000
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + a[i-1]*(j-1))
    ans = -1000000000
    for i in range(1, n+1):
        ans = max(ans, dp[i][m] + a[i-1]*m)
    return ans

if __name__ == '__main__':
    max_sum()