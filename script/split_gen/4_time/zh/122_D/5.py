def dfs(cur,prev1,prev2,prev3):
    if cur == N:
        return 1
    if dp[cur][prev1][prev2][prev3] != -1:
        return dp[cur][prev1][prev2][prev3]
    ret = 0
    for c in range(4):
        if ok(prev2,prev1,c):
            ret += dfs(cur+1,prev1,c,prev3)
            ret %= MOD
    dp[cur][prev1][prev2][prev3] = ret
    return ret
