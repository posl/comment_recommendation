def dfs(v):
    seen[v] = True
    for i in range(n):
        if graph[v][i] == 0:
            continue
        if seen[i]:
            continue
        dfs(i)
    return
n,m = map(int,input().split())
graph = [[0 for i in range(n)] for j in range(n)]
seen = [False for i in range(n)]
for i in range(m):
    u,v = map(int,input().split())
    graph[u-1][v-1] = 1
    graph[v-1][u-1] = 1
ans = 0
for i in range(n):
    if seen[i]:
        continue
    dfs(i)
    ans += 1
print(ans)
