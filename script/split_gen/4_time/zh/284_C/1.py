def dfs(v):
    visited[v] = True
    for i in range(n):
        if not visited[i] and graph[v][i]:
            dfs(i)
n,m = map(int,input().split())
graph = [[False for i in range(n)] for j in range(n)]
visited = [False for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    graph[a-1][b-1] = True
    graph[b-1][a-1] = True
count = 0
for i in range(n):
    if not visited[i]:
        dfs(i)
        count += 1
print(count)
