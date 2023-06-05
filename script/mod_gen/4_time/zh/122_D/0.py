def dfs(cur, prev1, prev2, prev3, dp):
    if dp[cur][prev1][prev2][prev3] >= 0:
        return dp[cur][prev1][prev2][prev3]
    if cur == N:
        return 1
    res = 0
    for c in range(4):
        if ok(c, prev1, prev2, prev3):
            res += dfs(cur + 1, c, prev1, prev2, dp)
            res %= MOD
    dp[cur][prev1][prev2][prev3] = res
    return res

if __name__ == '__main__':
    dfs()