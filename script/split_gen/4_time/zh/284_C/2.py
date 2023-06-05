def dfs(v):
    seen[v] = True
    for i in range(n):
        if not graph[v][i]:
            continue
        if seen[i]:
            continue
        dfs(i)
n, m = map(int, input().split())
graph = [[False] * n for _ in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u - 1][v - 1] = graph[v - 1][u - 1] = True
seen = [False] * n
count = 0
for v in range(n):
    if seen[v]:
        continue
    dfs(v)
    count += 1
print(count)
