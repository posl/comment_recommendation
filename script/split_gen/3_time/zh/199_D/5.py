def dfs(v, c):
    color[v] = c
    for i in range(len(G[v])):
        if color[G[v][i]] == c:
            return False
        if color[G[v][i]] == 0 and not dfs(G[v][i], -c):
            return False
    return True
N, M = map(int, input().split())
G = [[] for i in range(N)]
color = [0 for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
ans = 1
for i in range(N):
    if color[i] == 0:
        if not dfs(i, 1):
            ans = 0
            break
print(ans * 3 ** color.count(0))
