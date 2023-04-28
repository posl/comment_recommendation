Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)

    def dfs(v, c):
        color[v] = c
        for nv in g[v]:
            if color[nv] == c:
                return False
            if color[nv] == 0 and not dfs(nv, -c):
                return False
        return True

    color = [0] * n
    ans = 0
    for i in range(n):
        if color[i] == 0:
            if dfs(i, 1):
                b = sum(c == 1 for c in color)
                ans += b * (b - 1) // 2
                b = sum(c == -1 for c in color)
                ans += b * (b - 1) // 2
            else:
                print(0)
                exit()
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [0 for _ in range(N+1)]
    black = [0 for _ in range(N+1)]
    white = [0 for _ in range(N+1)]

    def dfs(v, color):
        visited[v] = 1
        if color == 0:
            black[v] = 1
        else:
            white[v] = 1

        for i in range(len(graph[v])):
            if visited[graph[v][i]] == 0:
                dfs(graph[v][i], 1-color)

    dfs(1, 0)

    black_count = sum(black)
    white_count = sum(white)
    print(black_count*white_count - M)

=======
Suggestion 3

def dfs(v, c):
    color[v] = c
    for i in g[v]:
        if color[i] == c:
            return False
        if color[i] == 0 and not dfs(i, -c):
            return False
    return True

n, m = map(int, input().split())
g = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
color = [0]*n
ans = 0
for i in range(n):
    if color[i] == 0:
        if dfs(i, 1):
            ans += 1
print(ans*(n-ans)-m)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(lambda x: int(x) - 1, input().split())
        graph[a].append(b)
        graph[b].append(a)

    from collections import deque
    def bfs(s):
        q = deque([s])
        dist = [None] * N
        dist[s] = 0
        while q:
            v = q.popleft()
            for nv in graph[v]:
                if dist[nv] is not None:
                    continue
                dist[nv] = dist[v] + 1
                q.append(nv)
        return dist

    d0 = bfs(0)
    d1 = bfs(N - 1)
    c0 = sum(1 for x in d0 if x % 2 == 0)
    c1 = N - c0
    ans = c0 * c1 - M
    print(ans)

=======
Suggestion 5

def dfs(v, c):
    color[v] = c
    for to in g[v]:
        if color[to] == c:
            return False
        if color[to] == 0 and not dfs(to, -c):
            return False
    return True

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
color = [0] * n
ans = 0
for i in range(n):
    if color[i] == 0:
        if dfs(i, 1):
            ans += 1
print(ans * (n - ans) - m)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    edges.sort(key=lambda x: x[0])
    edges.sort(key=lambda x: x[1])
    print(edges)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if (i+1, j+1) not in edges:
                print(i+1, j+1)
                count += 1
    print(count)

=======
Suggestion 7

def dfs(graph, v, color):
    color[v] = 1
    for i in graph[v]:
        if color[i] == 0:
            dfs(graph, i, color)
        elif color[i] == 1:
            return False
    color[v] = 2
    return True

n, m = map(int, input().split())
graph = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
color = [0 for i in range(n)]
ans = 0
for i in range(n):
    if color[i] == 0:
        if dfs(graph, i, color):
            ans += 1
print(ans)

=======
Suggestion 8

def bfs(graph, start):
    visited = [False] * len(graph)
    queue = [start]
    visited[start] = True
    while queue:
        v = queue.pop(0)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return visited

=======
Suggestion 9

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
edges.sort(key=lambda x: x[1])
parent = [i for i in range(N+1)]
ans = 0
for u, v in edges:
    if find_parent(parent, u) != find_parent(parent, v):
        ans += 1
        parent[find_parent(parent, u)] = find_parent(parent, v)
print(ans)

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]

    # 1. Create an adjacency list
    adj_list = [[] for _ in range(n)]
    for edge in edges:
        u, v = edge[0] - 1, edge[1] - 1
        adj_list[u].append(v)
        adj_list[v].append(u)

    # 2. Find the connected components
    visited = [False] * n
    components = []
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        component = [i]
        queue = [i]
        while queue:
            node = queue.pop()
            for neighbor in adj_list[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    component.append(neighbor)
                    queue.append(neighbor)
        components.append(component)

    # 3. Count the number of edges that connect different components
    ans = 0
    for component in components:
        num_nodes = len(component)
        num_edges = 0
        for node in component:
            num_edges += len(adj_list[node])
        num_edges //= 2
        num_internal_edges = num_edges - (num_nodes - 1)
        num_external_edges = num_nodes * (num_nodes - 1) // 2 - num_internal_edges
        ans += num_external_edges

    print(ans)
