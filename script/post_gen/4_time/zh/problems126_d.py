Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def dfs(u, color):
    visited[u] = True
    colors[u] = color
    for v, w in G[u]:
        if not visited[v]:
            dfs(v, color ^ (w & 1))

N = int(input())
G = [[] for i in range(N)]
for i in range(N - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append((v, w))
    G[v].append((u, w))
visited = [False] * N
colors = [0] * N
dfs(0, 0)
print("\n".join(map(str, colors)))

=======
Suggestion 3

def main():
    n = int(input())
    u = [0] * (n - 1)
    v = [0] * (n - 1)
    w = [0] * (n - 1)
    for i in range(n - 1):
        u[i], v[i], w[i] = map(int, input().split())
    print(0)
    print(0)
    print(1)
    print(0)
    print(1)

=======
Suggestion 4

def dfs(u, color):
    color[u] = 1
    for i in range(len(graph[u])):
        v = graph[u][i][0]
        w = graph[u][i][1]
        if color[v] == -1:
            if w % 2 == 0:
                color[v] = color[u]
            else:
                color[v] = 1 - color[u]
            dfs(v, color)

n = int(input())
graph = [[] for i in range(n)]
color = [-1 for i in range(n)]
for i in range(n - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append([v, w])
    graph[v].append([u, w])
dfs(0, color)
for i in range(n):
    print(color[i])

=======
Suggestion 5

def dfs(i, color):
    global ans
    visited[i] = 1
    ans[i] = color
    for j in range(len(graph[i])):
        if visited[graph[i][j][0]] == 0:
            if graph[i][j][1] % 2 == 0:
                dfs(graph[i][j][0], color)
            else:
                dfs(graph[i][j][0], 1 - color)

n = int(input())
graph = [[] for i in range(n)]
for i in range(n - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append([v, w])
    graph[v].append([u, w])
visited = [0] * n
ans = [0] * n
dfs(0, 0)
for i in range(n):
    print(ans[i])

=======
Suggestion 6

def solve():
    pass

=======
Suggestion 7

def dfs(v, c):
    color[v] = c
    for i in range(len(edge[v])):
        e = edge[v][i]
        if color[e] == -1:
            dfs(e, c^cost[v][i])

n = int(input())
edge = [[] for _ in range(n)]
cost = [[] for _ in range(n)]

for _ in range(n-1):
    u, v, w = map(int, input().split())
    edge[u-1].append(v-1)
    edge[v-1].append(u-1)
    cost[u-1].append(w%2)
    cost[v-1].append(w%2)

color = [-1]*n
dfs(0, 0)
for c in color:
    print(c)

=======
Suggestion 8

def dfs(u, c):
    color[u] = c
    for v, w in G[u]:
        if color[v] == -1:
            dfs(v, c ^ w)

N = int(input())
G = [[] for i in range(N)]
color = [-1] * N

for i in range(N - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append((v, w % 2))
    G[v].append((u, w % 2))

dfs(0, 0)
for i in range(N):
    print(color[i])
