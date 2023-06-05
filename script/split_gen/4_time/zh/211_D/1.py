def dfs(v):
    if v == N-1:
        return 1
    if dp[v] != -1:
        return dp[v]
    res = 0
    for i in range(len(G[v])):
        res += dfs(G[v][i])
        res %= mod
    dp[v] = res
    return res
N, M = map(int, input().split())
mod = 10**9+7
G = [[] for i in range(N)]
dp = [-1]*N
for i in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
print(dfs(0))
