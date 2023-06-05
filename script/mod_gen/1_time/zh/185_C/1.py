def solve(l):
    dp = [0 for _ in range(l+1)]
    dp[0] = 1
    for i in range(l):
        dp[i+1] += dp[i]
        if i+2 <= l:
            dp[i+2] += dp[i]
        if i+3 <= l:
            dp[i+3] += dp[i]
    return dp[l]

if __name__ == '__main__':
    solve()