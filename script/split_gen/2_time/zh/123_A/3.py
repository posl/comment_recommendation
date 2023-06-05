def dfs(cur, prev1, prev2, prev3):
    if cur == N:
        return 1
    if dp[cur][prev1][prev2][prev3] != -1:
        return dp[cur][prev1][prev2][prev3]
    ret = 0
    for c in range(4):
        if ok(prev1, prev2, prev3, c):
            ret += dfs(cur + 1, prev2, prev3, c)
            ret %= MOD
    dp[cur][prev1][prev2][prev3] = ret
    return ret
