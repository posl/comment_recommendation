Synthesizing 10/10 solutions

=======
Suggestion 1

def dfs(G, v, seen):
    seen[v] = True
    for next_v in G[v]:
        if seen[next_v]:
            continue
        dfs(G, next_v, seen)

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    G[u - 1].append(v - 1)
    G[v - 1].append(u - 1)

seen = [False] * N
count = 0
for v in range(N):
    if seen[v]:
        continue
    dfs(G, v, seen)
    count += 1
print(count)

=======
Suggestion 2

def dfs(graph, v, seen):
    seen[v] = True
    for next_v in graph[v]:
        if seen[next_v]:
            continue
        dfs(graph, next_v, seen)

=======
Suggestion 3

def dfs(v, visited, g):
    visited[v] = True
    for i in g[v]:
        if not visited[i]:
            dfs(i, visited, g)

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

visited = [False] * n
ans = 0
for i in range(n):
    if not visited[i]:
        dfs(i, visited, g)
        ans += 1
print(ans)

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]

    graph = [[] for _ in range(n + 1)]
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    visited = [False] * (n + 1)
    def dfs(v):
        visited[v] = True
        for next_v in graph[v]:
            if not visited[next_v]:
                dfs(next_v)

    count = 0
    for v in range(1, n + 1):
        if not visited[v]:
            dfs(v)
            count += 1

    print(count)

=======
Suggestion 5

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
for i in range(m):
    u, v = map(int, input().split())
    if u in graph:
        graph[u].add(v)
    else:
        graph[u] = set([v])
    if v in graph:
        graph[v].add(u)
    else:
        graph[v] = set([u])

for i in range(1, n+1):
    if i not in graph:
        graph[i] = set()
# print(graph)
count = 0

for i in range(1, n+1):
    if i in graph:
        if len(dfs(graph, i)) > 0:
            count += 1
print(count)

=======
Suggestion 6

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

visited = set()
count = 0

for i in range(n):
    if i not in visited:
        count += 1
        visited.update(dfs(graph, i))

print(count)

=======
Suggestion 7

def dfs(v):
    visited[v] = True
    for i in range(n):
        if not visited[i] and g[v][i]:
            dfs(i)

n, m = map(int, input().split())
g = [[False] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a-1][b-1] = g[b-1][a-1] = True

visited = [False] * n
ans = 0
for i in range(n):
    if not visited[i]:
        dfs(i)
        ans += 1

print(ans)

=======
Suggestion 8

def dfs(G, v, visited):
    visited[v] = True
    for next_v in G[v]:
        if visited[next_v] == False:
            dfs(G, next_v, visited)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        edges.append(tuple(map(int, input().split())))
    #print(edges)

    # make graph
    graph = [[0 for _ in range(N)] for _ in range(N)]
    for edge in edges:
        graph[edge[0]-1][edge[1]-1] = 1
        graph[edge[1]-1][edge[0]-1] = 1
    #print(graph)

    # count connected components
    count = 0
    visited = [False for _ in range(N)]
    for i in range(N):
        if visited[i]:
            continue
        count += 1
        queue = [i]
        while queue:
            v = queue.pop(0)
            visited[v] = True
            for j in range(N):
                if graph[v][j] == 1 and not visited[j]:
                    queue.append(j)
    print(count)

=======
Suggestion 10

def get_input():
    N, M = map(int, input().split())
    return N, M
