def solve(n, c):
    MOD = 10**9 + 7
    dp = [0] * (n + 1)
    dp[0] = 1
    last = {}
    for i in range(1, n + 1):
        dp[i] = dp[i - 1]
        if c[i - 1] in last and last[c[i - 1]] != i - 1:
            dp[i] += dp[last[c[i - 1]]]
        last[c[i - 1]] = i
        dp[i] %= MOD
    return dp[n]

if __name__ == '__main__':
    solve()