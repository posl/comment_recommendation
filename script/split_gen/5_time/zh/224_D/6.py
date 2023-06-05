def dfs(v, p):
    if v == 9:
        return p == 0
    if dp[v][p] != -1:
        return dp[v][p]
    dp[v][p] = 0
    for i in range(1, 9):
        if (p >> (i - 1)) & 1:
            for u in G[v]:
                if dfs(u, p ^ (1 << (i - 1))):
                    dp[v][p] = 1
    return dp[v][p]
