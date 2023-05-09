def solve(n, k, r, s, p, t):
    dp = [[0, 0, 0] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(3):
            if t[i-1] == 'r':
                if j == 0:
                    dp[i][j] = max(dp[i-1])
                else:
                    dp[i][j] = max(dp[i-1]) + p
            elif t[i-1] == 's':
                if j == 1:
                    dp[i][j] = max(dp[i-1])
                else:
                    dp[i][j] = max(dp[i-1]) + r
            else:
                if j == 2:
                    dp[i][j] = max(dp[i-1])
                else:
                    dp[i][j] = max(dp[i-1]) + s
        if i >= k:
            for j in range(3):
                dp[i][j] = max(dp[i][j], dp[i-k][j])
    return max(dp[n])

if __name__ == '__main__':
    solve()