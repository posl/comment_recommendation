def dfs(v, p):
    if v == 9:
        return 1
    if dp[v][p] != -1:
        return dp[v][p]
    res = INF
    for i in range(9):
        if i != p:
            res = min(res, dfs(v + 1, i) + (1 if not (v in G[i]) else 0))
    dp[v][p] = res
    return res
INF = 10 ** 9
M = int(input())
G = [[] for _ in range(9)]
for _ in range(M):
    u, v = map(int, input().split())
    G[u - 1].append(v - 1)
    G[v - 1].append(u - 1)
P = list(map(lambda x: int(x) - 1, input().split()))
dp = [[-1] * 9 for _ in range(9)]
ans = INF
for i in range(9):
    ans = min(ans, dfs(1, i) + (1 if not (1 in G[P[i]]) else 0))
print(ans if ans < INF else -1)

if __name__ == '__main__':
    dfs()