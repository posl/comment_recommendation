Synthesizing 10/10 solutions

=======
Suggestion 1

def dfs(node, color, color_id):
    color[node] = color_id
    for edge in graph[node]:
        if color[edge[0]] == -1:
            dfs(edge[0], color, color_id ^ edge[1])

N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    graph[u - 1].append((v - 1, w % 2))
    graph[v - 1].append((u - 1, w % 2))

color = [-1] * N
dfs(0, color, 0)
print(*color, sep="\n")

=======
Suggestion 2

def dfs(v, c):
    color[v] = c
    for i in range(len(edge[v])):
        if color[edge[v][i]] == -1:
            dfs(edge[v][i], c ^ w[v][i])

n = int(input())
edge = [[] for i in range(n)]
w = [[] for i in range(n)]
color = [-1 for i in range(n)]

for i in range(n - 1):
    u, v, weight = map(int, input().split())
    edge[u - 1].append(v - 1)
    edge[v - 1].append(u - 1)
    w[u - 1].append(weight % 2)
    w[v - 1].append(weight % 2)

dfs(0, 0)
for i in range(n):
    print(color[i])

=======
Suggestion 3

def dfs(v, p, c):
    color[v] = c
    for i in range(len(G[v])):
        if G[v][i] == p:
            continue
        if L[i] % 2 == 0:
            dfs(G[v][i], v, c)
        else:
            dfs(G[v][i], v, 1 - c)

n = int(input())
G = [[] for _ in range(n)]
L = [0] * (n - 1)
color = [0] * n
for i in range(n - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)
    L[i] = w

dfs(0, -1, 0)
for i in range(n):
    print(color[i])

=======
Suggestion 4

def dfs(u, c, color):
    color[u] = c
    for v, w in edge[u]:
        if color[v] == -1:
            dfs(v, c ^ w % 2, color)

n = int(input())
edge = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    edge[u - 1].append((v - 1, w))
    edge[v - 1].append((u - 1, w))
color = [-1] * n
dfs(0, 0, color)
for c in color:
    print(c)

=======
Suggestion 5

def main():
    pass

=======
Suggestion 6

def dfs(u, c):
    color[u] = c
    for v, w in g[u]:
        if color[v] == -1:
            dfs(v, c ^ w)

N = int(input())
g = [[] for _ in range(N)]
color = [-1] * N
for _ in range(N - 1):
    x, y, w = map(int, input().split())
    g[x - 1].append((y - 1, w % 2))
    g[y - 1].append((x - 1, w % 2))

dfs(0, 0)
for c in color:
    print(c)

=======
Suggestion 7

def dfs(node, color):
    global ans
    ans[node] = color
    for i in range(len(graph[node])):
        if ans[graph[node][i]] == -1:
            dfs(graph[node][i], color ^ cost[node][i])

n = int(input())
graph = [[] for _ in range(n)]
cost = [[] for _ in range(n)]
ans = [-1] * n
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)
    cost[u].append(w % 2)
    cost[v].append(w % 2)
dfs(0, 0)
for i in range(n):
    print(ans[i])

=======
Suggestion 8

def dfs(node, color):
    global colors, nodes, edges
    colors[node] = color
    for edge in edges[node]:
        if colors[edge[0]] == -1:
            dfs(edge[0], color ^ edge[1])

n = int(input())
nodes = []
for i in range(n):
    nodes.append([])
edges = {}
for i in range(n - 1):
    u, v, w = map(int, input().split())
    nodes[u - 1].append([v - 1, w % 2])
    nodes[v - 1].append([u - 1, w % 2])
    edges[i] = [u - 1, v - 1, w % 2]
colors = [-1 for i in range(n)]
dfs(0, 0)
for color in colors:
    print(color)

=======
Suggestion 9

def main():
    n = int(input())
    edges = []
    for i in range(n - 1):
        edges.append(list(map(int, input().split())))

    tree = [[] for i in range(n + 1)]
    for edge in edges:
        tree[edge[0]].append(edge[1])
        tree[edge[1]].append(edge[0])

    color = [-1] * (n + 1)
    color[1] = 0
    stack = [1]
    while stack:
        v = stack.pop()
        for u in tree[v]:
            if color[u] == -1:
                color[u] = color[v] ^ 1
                stack.append(u)

    for v in range(1, n + 1):
        print(color[v])

=======
Suggestion 10

def main():
    print('hello world')
