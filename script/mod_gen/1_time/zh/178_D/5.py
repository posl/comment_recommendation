def dfs(s, depth):
    if s < 0:
        return 0
    if s == 0:
        return 1
    if depth == 0:
        return 0
    if dp[s][depth] != -1:
        return dp[s][depth]
    dp[s][depth] = 0
    for i in range(3, s+1):
        dp[s][depth] += dfs(s-i, depth-1)
    return dp[s][depth]
MOD = 10**9 + 7
S = int(input())
dp = [[-1 for _ in range(S+1)] for _ in range(S+1)]
print(dfs(S, S) % MOD)
