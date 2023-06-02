Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def dfs(u, color):
    color[u] = 1
    for v, w in edges[u]:
        if color[v] == -1:
            color[v] = color[u] ^ w
            dfs(v, color)

n = int(input())
edges = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append((v, w % 2))
    edges[v].append((u, w % 2))

color = [-1] * n
dfs(0, color)
print(*color, sep='\n')

=======
Suggestion 3

def dfs(u, c):
    color[u] = c
    for i in range(len(G[u])):
        v = G[u][i][0]
        if color[v] == -1:
            if G[u][i][1] % 2 == 0:
                dfs(v, c)
            else:
                dfs(v, 1 - c)

N = int(input())
G = [[] for i in range(N)]
color = [-1 for i in range(N)]
for i in range(N - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append((v, w))
    G[v].append((u, w))
dfs(0, 0)
for i in range(N):
    print(color[i])

=======
Suggestion 4

def dfs(v, c):
    color[v] = c
    for i in range(len(G[v])):
        if color[G[v][i]] == -1:
            dfs(G[v][i], c ^ 1)

N = int(input())
G = [[] for i in range(N)]
color = [-1] * N
for i in range(N - 1):
    u, v, w = [int(x) for x in input().split()]
    u -= 1
    v -= 1
    if w % 2 == 0:
        G[u].append(v)
        G[v].append(u)
dfs(0, 0)
for i in range(N):
    print(color[i])

=======
Suggestion 5

def dfs(u, c):
    color[u] = c
    for i in range(len(edge[u])):
        v = edge[u][i]
        if color[v] == -1:
            dfs(v, c ^ 1)

n = int(input())
edge = [[] for i in range(n)]
color = [-1] * n
for i in range(n - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    if w % 2 == 0:
        edge[u].append(v)
        edge[v].append(u)

dfs(0, 0)
for i in range(n):
    print(color[i])

=======
Suggestion 6

def dfs(u, c, d):
    color[u] = c
    depth[u] = d
    for v in G[u]:
        if depth[v] == -1:
            dfs(v, c^1, d+1)

n = int(input())
G = [[] for _ in range(n)]
for _ in range(n-1):
    u, v, w = map(int, input().split())
    G[u-1].append(v-1)
    G[v-1].append(u-1)

color = [-1] * n
depth = [-1] * n
dfs(0, 0, 0)

for i in range(n):
    print(color[i])

=======
Suggestion 7

def dfs(node, color):
    global colors
    colors[node] = color
    for v, w in graph[node]:
        if colors[v] == -1:
            dfs(v, color ^ w % 2)

n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    graph[u - 1].append((v - 1, w))
    graph[v - 1].append((u - 1, w))

colors = [-1] * n
dfs(0, 0)
for i in range(n):
    print(colors[i])

=======
Suggestion 8

def dfs(v, c):
    color[v] = c
    for i in range(len(G[v])):
        if color[G[v][i]] == -1:
            dfs(G[v][i], 1 - c)

N = int(input())
G = [[] for _ in range(N)]
color = [-1] * N
for _ in range(N-1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    if w % 2 == 0:
        G[u].append(v)
        G[v].append(u)
dfs(0, 0)
for i in range(N):
    print(color[i])

=======
Suggestion 9

def dfs(s, c):
    color[s] = c
    for i in range(len(g[s])):
        if color[g[s][i]] == -1:
            dfs(g[s][i], c ^ d[s][i])

n = int(input())
g = [[] for _ in range(n)]
d = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    g[u - 1].append(v - 1)
    g[v - 1].append(u - 1)
    d[u - 1].append(w % 2)
    d[v - 1].append(w % 2)

color = [-1] * n
dfs(0, 0)
for i in range(n):
    print(color[i])

=======
Suggestion 10

def get_color(n,edges):
    """edges: list of tuple"""
    color = [None] * n
    color[0] = 0
    stack = [0]
    while stack:
        node = stack.pop()
        for edge in edges:
            if edge[0] == node:
                if color[edge[1]-1] is None:
                    color[edge[1]-1] = color[node] ^ edge[2] & 1
                    stack.append(edge[1]-1)
    return color
