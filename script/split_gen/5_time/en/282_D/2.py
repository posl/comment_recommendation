def dfs(v, c):
    color[v] = c
    for i in range(len(g[v])):
        if color[g[v][i]] == c:
            return False
        if color[g[v][i]] == 0 and not dfs(g[v][i], -c):
            return False
    return True
N, M = map(int, input().split())
g = [[] for i in range(N)]
color = [0 for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
ans = 0
for i in range(N):
    if color[i] == 0:
        if dfs(i, 1):
            ans += 1
print(ans * (N - ans) - M)
