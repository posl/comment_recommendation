def dfs(node, prev, dist):
    global dists
    dists[node] = dist
    for n in graph[node]:
        if n != prev:
            dfs(n, node, dist+1)
n, x, y = map(int, input().split())
x, y = x-1, y-1
graph = [[] for _ in range(n)]
for _ in range(n-1):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    graph[u].append(v)
    graph[v].append(u)
dists = [0] * n
dfs(x, -1, 0)
print(dists[y])
