def dfs(node):
    if node in visited:
        return
    else:
        visited.add(node)
        for child in graph[node]:
            dfs(child)
n, m = map(int, input().split())
graph = {}
for i in range(n):
    graph[i+1] = []
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
visited = set()
ans = 0
for i in range(n):
    if i+1 not in visited:
        ans += 1
        dfs(i+1)
print(ans)

if __name__ == '__main__':
    dfs()