Synthesizing 10/10 solutions

=======
Suggestion 1

def dfs(v):
    seen[v] = True
    for next_v in graph[v]:
        if seen[next_v]:
            continue
        dfs(next_v)

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

seen = [False] * N
count = 0
for v in range(N):
    if seen[v]:
        continue
    count += 1
    dfs(v)
print(count)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u-1].append(v-1)
        G[v-1].append(u-1)
    visited = [False] * N
    def dfs(v):
        visited[v] = True
        for nv in G[v]:
            if not visited[nv]:
                dfs(nv)
    count = 0
    for v in range(N):
        if not visited[v]:
            dfs(v)
            count += 1
    print(count)

=======
Suggestion 3

def dfs(v):
    seen[v] = True
    for next_v in graph[v]:
        if seen[next_v]:
            continue
        dfs(next_v)

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

seen = [False] * n
count = 0
for v in range(n):
    if seen[v]:
        continue
    dfs(v)
    count += 1
print(count)

=======
Suggestion 4

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
visited = [False] * N
for _ in range(M):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

ans = 0
for i in range(N):
    if not visited[i]:
        dfs(i)
        ans += 1
print(ans)

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

=======
Suggestion 6

def dfs(v, visited, graph):
    visited[v] = True
    for i in range(len(graph[v])):
        if not visited[graph[v][i]]:
            dfs(graph[v][i], visited, graph)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False for _ in range(n + 1)]
ans = 0
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i, visited, graph)
        ans += 1

print(ans)

=======
Suggestion 7

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in graph[vertex]:
                stack.append(neighbor)
    return visited

N, M = map(int, input().split())
graph = {i:[] for i in range(1, N+1)}
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0
visited = set()
for vertex in range(1, N+1):
    if vertex not in visited:
        count += 1
        visited = visited | dfs(graph, vertex)
print(count)

=======
Suggestion 8

def dfs(v):
    visited[v] = True
    for i in range(n):
        if not visited[i] and graph[v][i]:
            dfs(i)

n, m = map(int, input().split())
graph = [[False] * n for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = graph[b-1][a-1] = True

visited = [False] * n
ans = 0
for i in range(n):
    if not visited[i]:
        dfs(i)
        ans += 1
print(ans)

=======
Suggestion 9

def dfs(v):
    visited[v] = True
    for i in range(n):
        if not visited[i] and graph[v][i]:
            dfs(i)

n,m = map(int, input().split())
graph = [[False] * n for i in range(n)]
for i in range(m):
    u,v = map(int, input().split())
    graph[u-1][v-1] = True
    graph[v-1][u-1] = True

visited = [False] * n
count = 0
for i in range(n):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)

=======
Suggestion 10

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
