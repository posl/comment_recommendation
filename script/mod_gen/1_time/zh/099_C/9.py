def solve(n):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        j = 1
        while i - j >= 0:
            dp[i] = min(dp[i], dp[i - j] + 1)
            j *= 6
        j = 1
        while i - j >= 0:
            dp[i] = min(dp[i], dp[i - j] + 1)
            j *= 9
    return dp[n]

if __name__ == '__main__':
    solve()