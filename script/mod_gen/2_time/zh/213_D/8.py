def dfs(v, visited, graph, ans):
    visited[v] = True
    ans.append(v)
    for i in range(len(graph[v])):
        if not visited[graph[v][i]]:
            dfs(graph[v][i], visited, graph, ans)
            ans.append(v)
n = int(input())
graph = [[] for i in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
for i in range(n):
    graph[i].sort()
visited = [False] * n
ans = []
dfs(0, visited, graph, ans)
print(*[i+1 for i in ans])

if __name__ == '__main__':
    dfs()