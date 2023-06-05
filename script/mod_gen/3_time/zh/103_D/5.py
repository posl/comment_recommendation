def dfs(x, y):
    global n, m, a, b, visited, graph
    visited[x] = True
    for i in range(len(graph[x])):
        if graph[x][i] == y:
            graph[x][i] = 0
            graph[y][i] = 0
            return
    for i in range(len(graph[x])):
        if graph[x][i] != 0 and visited[graph[x][i]] == False:
            dfs(graph[x][i], y)
n, m = map(int, input().split())
a = []
b = []
for i in range(m):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)
graph = [[] for _ in range(n+1)]
for i in range(m):
    graph[a[i]].append(b[i])
    graph[b[i]].append(a[i])
ans = 0
for i in range(m):
    visited = [False for _ in range(n+1)]
    dfs(a[i], b[i])
    if visited.count(True) != n:
        ans += 1
print(ans)

if __name__ == '__main__':
    dfs()