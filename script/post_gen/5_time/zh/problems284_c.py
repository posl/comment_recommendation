Synthesizing 10/10 solutions

=======
Suggestion 1

def dfs(i, used, graph):
    used[i] = True
    for j in graph[i]:
        if not used[j]:
            dfs(j, used, graph)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        edges.append(tuple(map(int, input().split())))
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    visited = [False for _ in range(n)]
    def dfs(u):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs(v)
    count = 0
    for u in range(n):
        if not visited[u]:
            count += 1
            dfs(u)
    print(count)

=======
Suggestion 3

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


n, m = map(int, input().split())
graph = {}
for i in range(n):
    graph[i+1] = set()
for i in range(m):
    u, v = map(int, input().split())
    graph[u].add(v)
    graph[v].add(u)
count = 0
visited = set()
for i in range(1, n+1):
    if i not in visited:
        visited.update(dfs(graph, i))
        count += 1
print(count)

=======
Suggestion 4

def dfs(v):
    visited[v] = True
    for i in range(n):
        if not visited[i] and g[v][i] == 1:
            dfs(i)

n, m = map(int, input().split())
g = [[0 for i in range(n)] for j in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    g[u - 1][v - 1] = g[v - 1][u - 1] = 1
visited = [False for i in range(n)]
ans = 0
for i in range(n):
    if not visited[i]:
        dfs(i)
        ans += 1
print(ans)

=======
Suggestion 5

def dfs(v):
    seen[v] = True
    for i in range(1,n+1):
        if not seen[i] and g[v][i] == 1:
            dfs(i)

n,m = map(int,input().split())
g = [[0 for i in range(n+1)] for j in range(n+1)]
seen = [False for i in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    g[a][b] = g[b][a] = 1

ans = 0
for i in range(1,n+1):
    if not seen[i]:
        dfs(i)
        ans += 1
print(ans)

=======
Suggestion 6

def dfs(v):
    seen[v] = True
    for next_v in range(n):
        if graph[v][next_v] == 0:
            continue
        if seen[next_v]:
            continue
        dfs(next_v)

n, m = map(int, input().split())
graph = [[0] * n for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u][v] = graph[v][u] = 1

seen = [False] * n
ans = 0
for v in range(n):
    if seen[v]:
        continue
    dfs(v)
    ans += 1

print(ans)

=======
Suggestion 7

def dfs(v):
    seen[v] = True
    for next_v in graph[v]:
        if seen[next_v]:
            continue
        dfs(next_v)

N, M = map(int, input().split())
graph = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

seen = [False] * N
count = 0
for v in range(N):
    if seen[v]:
        continue
    dfs(v)
    count += 1

print(count)

=======
Suggestion 8

def dfs(v):
    seen[v] = True
    for i in range(n):
        if not seen[i] and G[v][i] == 1:
            dfs(i)

n, m = map(int, input().split())
G = [[0] * n for _ in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    G[u-1][v-1] = G[v-1][u-1] = 1

seen = [False] * n
res = 0
for i in range(n):
    if not seen[i]:
        dfs(i)
        res += 1

print(res)

=======
Suggestion 9

def dfs(v):
    seen[v] = True
    for nv in g[v]:
        if seen[nv]:
            continue
        dfs(nv)

=======
Suggestion 10

def set_adjacency_matrix(N, M, u, v):
    adjacency_matrix = [[0 for i in range(N)] for j in range(N)]
    for i in range(M):
        adjacency_matrix[u[i]-1][v[i]-1] = 1
        adjacency_matrix[v[i]-1][u[i]-1] = 1
    return adjacency_matrix
