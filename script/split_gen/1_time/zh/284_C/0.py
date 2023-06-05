def dfs(u):
    global n
    global m
    global g
    global visited
    global flag
    visited[u] = True
    for i in range(n):
        if not visited[i] and g[u][i] == 1:
            dfs(i)
    flag = True
n, m = [int(i) for i in input().split()]
g = [[0 for i in range(n)] for j in range(n)]
for i in range(m):
    u, v = [int(i) for i in input().split()]
    g[u - 1][v - 1] = 1
    g[v - 1][u - 1] = 1
visited = [False for i in range(n)]
ans = 0
for i in range(n):
    if not visited[i]:
        flag = False
        dfs(i)
        if flag:
            ans += 1
print(ans)
