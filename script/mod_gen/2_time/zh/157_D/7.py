def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
n, m, k = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
for _ in range(k):
    c, d = map(int, input().split())
    graph[c-1].append(d-1)
    graph[d-1].append(c-1)
visited = [False for _ in range(n)]
ans = [0 for _ in range(n)]
for i in range(n):
    if not visited[i]:
        dfs(graph, i, visited)
    ans[i] = visited.count(False) - 1
    visited = [False for _ in range(n)]
print(*ans)

if __name__ == '__main__':
    dfs()