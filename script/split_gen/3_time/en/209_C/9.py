def solve(n, c):
    mod = 10**9 + 7
    # dp[i]: number of sequences satisfying the conditions
    dp = [1] * n
    # cum[i]: cumulative sum of dp[i]
    cum = [0] * n
    cum[0] = dp[0]
    for i in range(1, n):
        cum[i] = cum[i - 1] + dp[i]
    # last[j]: the last index of j
    last = [-1] * (max(c) + 1)
    for i in range(n):
        last[c[i]] = i
    for i in range(1, n):
        if c[i - 1] == c[i]:
            dp[i] = cum[i - 1]
        elif last[c[i]] < i - 1:
            dp[i] = cum[i - 1]
        else:
            dp[i] = (cum[i - 1] - cum[last[c[i]] - 1]) % mod
    return dp[-1]
