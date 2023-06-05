def dfs(v, c):
    seen[v] = c
    for vv in graph[v]:
        if seen[vv]:
            continue
        dfs(vv, c)
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)
seen = [0] * N
c = 0
for v in range(N):
    if seen[v]:
        continue
    c += 1
    dfs(v, c)
print(c)
