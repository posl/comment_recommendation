def dfs(v, c):
    color[v] = c
    for i in range(0, len(G[v])):
        if color[G[v][i]] == c:
            return False
        if color[G[v][i]] == 0 and dfs(G[v][i], -c) == False:
            return False
    return True
N, M = map(int, input().split())
G = [[] for i in range(0, N)]
color = [0 for i in range(0, N)]
for i in range(0, M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
ans = 1
for i in range(0, N):
    if color[i] == 0:
        if dfs(i, 1) == False:
            ans = 0
            break
print(ans * 3 ** color.count(0))
