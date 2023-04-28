Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    tree = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        tree[u-1].append((v-1, w))
        tree[v-1].append((u-1, w))
    Q = [(0, 0)]
    color = [-1] * N
    color[0] = 0
    while Q:
        v, c = Q.pop()
        for u, w in tree[v]:
            if color[u] != -1:
                continue
            color[u] = (c + w) % 2
            Q.append((u, color[u]))
    print(*color, sep="\n")

=======
Suggestion 2

def dfs(v, c):
    color[v] = c
    for next_v, w in graph[v]:
        if color[next_v] != -1:
            continue
        if w % 2 == 0:
            dfs(next_v, c)
        else:
            dfs(next_v, 1 - c)

n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    graph[u - 1].append((v - 1, w))
    graph[v - 1].append((u - 1, w))

color = [-1] * n
dfs(0, 0)

for c in color:
    print(c)

=======
Suggestion 3

def main():
    N = int(input())
    G = [[] for i in range(N)]
    for i in range(N-1):
        u,v,w = map(int,input().split())
        u -= 1
        v -= 1
        G[u].append((v,w))
        G[v].append((u,w))
    color = [0] * N
    def dfs(u,p,c):
        color[u] = c
        for v,w in G[u]:
            if v == p:
                continue
            if w % 2 == 0:
                dfs(v,u,c)
            else:
                dfs(v,u,1-c)
    dfs(0,-1,0)
    for i in range(N):
        print(color[i])

=======
Suggestion 4

def dfs(v, c):
    color[v] = c
    for i in graph[v]:
        if color[i] == -1:
            dfs(i, 1 - c)

N = int(input())
graph = [[] for _ in range(N)]
color = [-1] * N
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    if w % 2 == 0:
        graph[u].append(v)
        graph[v].append(u)
dfs(0, 0)
for i in range(N):
    print(color[i])

=======
Suggestion 5

def dfs(x, c):
    color[x] = c
    for y, w in edges[x]:
        if color[y] == -1:
            dfs(y, c ^ w)

n = int(input())
edges = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    edges[u - 1].append((v - 1, w % 2))
    edges[v - 1].append((u - 1, w % 2))

color = [-1] * n
dfs(0, 0)
for i in range(n):
    print(color[i])

=======
Suggestion 6

def main():
    N = int(input())
    edges = []
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    #print(edges)
    colors = [-1]*(N+1)
    colors[1] = 0
    #print(colors)
    queue = [1]
    while queue:
        #print(queue)
        now = queue.pop(0)
        for u, v, w in edges:
            if u == now and colors[v] == -1:
                if w % 2 == 0:
                    colors[v] = colors[u]
                else:
                    colors[v] = 1 - colors[u]
                queue.append(v)
            elif v == now and colors[u] == -1:
                if w % 2 == 0:
                    colors[u] = colors[v]
                else:
                    colors[u] = 1 - colors[v]
                queue.append(u)
    for i in range(1, N+1):
        print(colors[i])

=======
Suggestion 7

def main():
    n = int(input())
    edges = []
    for _ in range(n-1):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    #print(edges)
    g = [[] for _ in range(n+1)]
    for u, v, w in edges:
        g[u].append((v, w))
        g[v].append((u, w))
    #print(g)
    color = [0] * (n+1)
    color[1] = 0
    q = [1]
    while len(q) > 0:
        u = q.pop()
        for v, w in g[u]:
            if color[v] == 0:
                if w % 2 == 0:
                    color[v] = color[u]
                else:
                    color[v] = 1 - color[u]
                q.append(v)
    for i in range(1, n+1):
        print(color[i])

main()

=======
Suggestion 8

def dfs(G, v, p, d):
    color[v] = d
    for next_v in G[v]:
        if next_v == p:
            continue
        dfs(G, next_v, v, d ^ 1)

=======
Suggestion 9

def dfs(now, color, g, ans):
    ans[now] = color
    for next in g[now]:
        if ans[next] == -1:
            dfs(next, 1 - color, g, ans)

N = int(input())
g = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    if w % 2 == 0:
        g[u].append(v)
        g[v].append(u)
ans = [-1] * N
dfs(0, 0, g, ans)
for i in range(N):
    print(ans[i])

=======
Suggestion 10

def dfs(node,par,dist,color):
    color[node] = dist % 2
    for i in edge[node]:
        if i == par:
            continue
        dfs(i,node,dist+1,color)

n = int(input())
edge = [[] for i in range(n)]
color = [0 for i in range(n)]
for i in range(n-1):
    u,v,w = map(int,input().split())
    edge[u-1].append(v-1)
    edge[v-1].append(u-1)
dfs(0,-1,0,color)
for i in color:
    print(i)
