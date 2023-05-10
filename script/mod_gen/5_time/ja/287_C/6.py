def dfs(v):
    visited[v] = True
    for next_v in graph[v]:
        if visited[next_v]:
            continue
        dfs(next_v)
    return
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [False] * (N+1)
dfs(1)
print("Yes" if all(visited) else "No")

if __name__ == '__main__':
    dfs()