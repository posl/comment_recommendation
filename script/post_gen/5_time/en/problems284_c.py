Synthesizing 10/10 solutions

=======
Suggestion 1

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
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

seen = [False] * n
ans = 0
for v in range(n):
    if seen[v]:
        continue
    dfs(v)
    ans += 1
print(ans)

=======
Suggestion 2

def find_parent(parent, i):
    if parent[i] == -1:
        return i
    if parent[i] != -1:
        return find_parent(parent, parent[i])

=======
Suggestion 3

def main():
    from collections import defaultdict
    n, m = map(int, input().split())
    g = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)

    visited = [False] * (n + 1)

    def dfs(v):
        visited[v] = True
        for i in g[v]:
            if not visited[i]:
                dfs(i)

    ans = 0
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
            ans += 1
    print(ans)

=======
Suggestion 4

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

=======
Suggestion 5

def dfs(v, seen, g):
    seen[v] = True
    for next_v in g[v]:
        if seen[next_v]:
            continue
        dfs(next_v, seen, g)

=======
Suggestion 6

def dfs(v, G, seen):
    seen[v] = True
    for next_v in G[v]:
        if seen[next_v]: continue
        dfs(next_v, G, seen)

=======
Suggestion 7

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    stack.append(neighbor)
    return visited

n, m = map(int, input().split())
graph = [set() for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].add(v)
    graph[v].add(u)
ans = 0
for i in range(1, n+1):
    if i not in graph[i]:
        ans += 1
        dfs(graph, i)
print(ans)

=======
Suggestion 8

def dfs(v):
    seen[v] = True
    for i in range(1, N+1):
        if not seen[i] and G[v][i]:
            dfs(i)

N, M = map(int, input().split())
G = [[False] * (N+1) for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    G[u][v] = G[v][u] = True

seen = [False] * (N+1)
ans = 0
for i in range(1, N+1):
    if not seen[i]:
        dfs(i)
        ans += 1

print(ans)

=======
Suggestion 9

def main():
    n,m = map(int, input().split())
    edges = []
    for i in range(m):
        edges.append(list(map(int, input().split())))
    #print(edges)
    graph = [[] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if edges[j][0] == i+1:
                graph[i].append(edges[j][1])
            if edges[j][1] == i+1:
                graph[i].append(edges[j][0])
    #print(graph)
    visited = [False for i in range(n)]
    def dfs(graph, v, visited):
        visited[v] = True
        for i in range(len(graph[v])):
            if not visited[graph[v][i]-1]:
                dfs(graph, graph[v][i]-1, visited)
    count = 0
    for i in range(n):
        if not visited[i]:
            count += 1
            dfs(graph, i, visited)
    print(count)

=======
Suggestion 10

def main():
    n,m = map(int, input().split())
    edges = []
    for i in range(m):
        edges.append(list(map(int, input().split())))
    print(n - m)
