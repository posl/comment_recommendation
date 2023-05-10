def dfs(v, color):
    colors[v] = color
    for i in G[v]:
        if colors[i] == color:
            return False
        if colors[i] == 0 and not dfs(i, -color):
            return False
    return True
N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
colors = [0]*N
ans = 0
for i in range(N):
    if colors[i] == 0:
        if dfs(i, 1):
            ans += 1
print(ans)
