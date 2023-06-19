def dfs(v):
    global cnt
    global visited
    visited[v] = True
    for i in range(1, n+1):
        if visited[i] == False and G[v][i] == 1:
            dfs(i)
n, m = map(int, input().split())
G = [[0] * (n+1) for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    G[a][b] = 1
    G[b][a] = 1
cnt = 0
visited = [False] * (n+1)
for i in range(1, n+1):
    if visited[i] == False:
        dfs(i)
        cnt += 1
print(cnt)
