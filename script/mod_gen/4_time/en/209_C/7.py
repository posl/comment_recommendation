def solve(n, c):
    mod = 10**9 + 7
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(1, n+1):
        dp[i] = dp[i-1] * (c[i-1] - i + 1) % mod
    return dp[n]

if __name__ == '__main__':
    solve()