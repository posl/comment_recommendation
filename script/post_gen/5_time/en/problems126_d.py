Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    graph = [[] for i in range(N)]
    for i in range(N-1):
        u, v, w = map(int, input().split())
        graph[u-1].append((v-1, w))
        graph[v-1].append((u-1, w))

    color = [-1] * N
    color[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for (nv, w) in graph[v]:
            if color[nv] != -1:
                continue
            color[nv] = (color[v] + w) % 2
            stack.append(nv)

    print(*color, sep='\n')

=======
Suggestion 2

def dfs(v, c):
    color[v] = c
    for i in range(len(tree[v])):
        if color[tree[v][i][0]] == -1:
            if tree[v][i][1] % 2 == 0:
                dfs(tree[v][i][0], c)
            else:
                dfs(tree[v][i][0], 1-c)

n = int(input())
tree = [[] for i in range(n)]
for i in range(n-1):
    u, v, w = map(int, input().split())
    tree[u-1].append((v-1, w))
    tree[v-1].append((u-1, w))
color = [-1] * n
dfs(0, 0)
for i in range(n):
    print(color[i])

=======
Suggestion 3

def bfs(graph, start):
    visited, queue = [], [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(graph[vertex])
    return visited

=======
Suggestion 4

def dfs(x, c):
    color[x] = c
    for y, w in edge[x]:
        if color[y] == -1:
            dfs(y, c ^ w)

n = int(input())
edge = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    edge[u].append((v, w % 2))
    edge[v].append((u, w % 2))

color = [-1] * n
dfs(0, 0)
print(*color, sep='\n')

=======
Suggestion 5

def dfs(v, c):
    color[v] = c
    for u, w in tree[v]:
        if color[u] == -1:
            dfs(u, c ^ w % 2)

N = int(input())
tree = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    tree[u - 1].append((v - 1, w))
    tree[v - 1].append((u - 1, w))

color = [-1] * N
dfs(0, 0)
print(*color, sep='\n')

=======
Suggestion 6

def dfs(v, p, d):
    for i in G[v]:
        if i == p:
            continue
        if d % 2 == 0:
            color[i] = 0
        else:
            color[i] = 1
        dfs(i, v, d + 1)

N = int(input())
G = [[] for i in range(N)]
color = [0] * N

for i in range(N - 1):
    u, v, w = map(int, input().split())
    G[u - 1].append(v - 1)
    G[v - 1].append(u - 1)

color[0] = 0
dfs(0, -1, 0)

for i in color:
    print(i)

=======
Suggestion 7

def main():
    N = int(input())
    edges = []
    for i in range(N-1):
        edges.append(list(map(int, input().split())))
    nodes = [-1 for i in range(N+1)]
    nodes[1] = 0
    for edge in edges:
        if nodes[edge[0]] == -1:
            nodes[edge[0]] = nodes[edge[1]] + edge[2]
        elif nodes[edge[1]] == -1:
            nodes[edge[1]] = nodes[edge[0]] + edge[2]
        else:
            nodes[edge[0]] = nodes[edge[1]] + edge[2]
    for i in range(1, N+1):
        print(nodes[i]%2)

=======
Suggestion 8

def dfs(v, p, d):
    global color
    color[v] = d
    for i in range(len(e[v])):
        if e[v][i] == p:
            continue
        if w[v][i] % 2 == 0:
            dfs(e[v][i], v, d)
        else:
            dfs(e[v][i], v, 1 - d)

n = int(input())
e = [[] for _ in range(n)]
w = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v, ww = map(int, input().split())
    e[u - 1].append(v - 1)
    e[v - 1].append(u - 1)
    w[u - 1].append(ww)
    w[v - 1].append(ww)
color = [-1] * n
dfs(0, -1, 0)
for i in range(n):
    print(color[i])

=======
Suggestion 9

def paint_tree(tree, color, node, parent, dist):
    color[node] = (color[parent] + dist) % 2
    for child, dist in tree[node]:
        if child == parent:
            continue
        paint_tree(tree, color, child, node, dist)

=======
Suggestion 10

def main():
    N = int(input())
    edges = []
    for i in range(0, N-1):
        edges.append(list(map(int, input().split())))
    
    #print(edges)
    #print(N)
    
    # color[v] = 0 or 1
    color = [-1] * (N+1)
    color[1] = 0
    
    # bfs
    queue = [1]
    while len(queue) > 0:
        #print(queue)
        v = queue.pop(0)
        #print(v)
        for edge in edges:
            if edge[0] == v:
                #print(edge[1])
                if color[edge[1]] == -1:
                    color[edge[1]] = (color[edge[0]] + edge[2]) % 2
                    queue.append(edge[1])
            elif edge[1] == v:
                #print(edge[0])
                if color[edge[0]] == -1:
                    color[edge[0]] = (color[edge[1]] + edge[2]) % 2
                    queue.append(edge[0])
            else:
                continue

    #print(color)
    for c in color[1:]:
        print(c)
