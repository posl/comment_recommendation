def dfs(v, p, d):
    global depth
    depth[v] = d
    for i in graph[v]:
        if i == p:
            continue
        dfs(i, v, d + 1)
n, q = map(int, input().split())
graph = [[] for i in range(n + 1)]
depth = [0] * (n + 1)
for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
dfs(1, 0, 0)
ans = [0] * (n + 1)
for i in range(q):
    p, x = map(int, input().split())
    ans[p] += x
for i in range(1, n + 1):
    print(ans[i])
