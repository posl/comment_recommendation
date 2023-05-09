Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N,X,Y = map(int,input().split())
    U = []
    V = []
    for i in range(N-1):
        u,v = map(int,input().split())
        U.append(u)
        V.append(v)
    ans = [0]*(N-1)
    for i in range(N-1):
        for j in range(i+1,N):
            if i+1 == j:
                continue
            if U[i] == X and V[i] == Y and U[j] == X and V[j] == Y:
                ans[i] += 1
                ans[j] += 1
            elif U[i] == X and V[i] == Y:
                ans[i] += 1
            elif U[j] == X and V[j] == Y:
                ans[j] += 1
            elif U[i] == X and U[j] == Y:
                ans[i] += 1
                ans[j] += 1
            elif U[i] == Y and U[j] == X:
                ans[i] += 1
                ans[j] += 1
            elif V[i] == X and V[j] == Y:
                ans[i] += 1
                ans[j] += 1
            elif V[i] == Y and V[j] == X:
                ans[i] += 1
                ans[j] += 1
    for i in range(N-1):
        print(ans[i])

=======
Suggestion 2

def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        G[u].append(v)
        G[v].append(u)
    dist = [N] * N
    dist[X] = 0
    que = [X]
    while que:
        q = que.pop()
        for v in G[q]:
            if dist[v] > dist[q] + 1:
                dist[v] = dist[q] + 1
                que.append(v)
    print(dist[Y])

=======
Suggestion 3

def main():
    N, X, Y = map(int, input().split())
    X, Y = X-1, Y-1
    edges = [list(map(int, input().split())) for _ in range(N-1)]
    graph = [[] for _ in range(N)]
    for u, v in edges:
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)

    from collections import deque
    def bfs(graph, start):
        dist = [-1] * N
        dist[start] = 0
        queue = deque([start])
        while queue:
            v = queue.popleft()
            for nv in graph[v]:
                if dist[nv] != -1:
                    continue
                dist[nv] = dist[v] + 1
                queue.append(nv)
        return dist

    dist = bfs(graph, X)
    print(dist[Y])
    return

main()

=======
Suggestion 4

def dfs(v, p, g, d):
    for nv in g[v]:
        if nv == p:
            continue
        d[nv] = d[v] + 1
        dfs(nv, v, g, d)

n, x, y = map(int, input().split())
x -= 1
y -= 1
g = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

d = [0]*n
dfs(x, -1, g, d)
print(d[y])

=======
Suggestion 5

def dfs(v, p):
    for u in graph[v]:
        if u == p: continue
        dist[u] = dist[v] + 1
        dfs(u, v)

n, x, y = map(int, input().split())
x -= 1
y -= 1
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)
dist = [0] * n
dfs(x, -1)
print(*dist)

=======
Suggestion 6

def read_ints():
    return list(map(int, input().split()))

N, X, Y = read_ints()
edges = []
for i in range(N-1):
    edges.append(read_ints())

=======
Suggestion 7

def dfs(v,p):
    global ans
    ans.append(v)
    for u in G[v]:
        if u != p:
            dfs(u,v)
            ans.append(v)
    return

N,X,Y = map(int,input().split())
X -= 1
Y -= 1
G = [[] for i in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

ans = []
dfs(X,-1)
ans = ans[::-1]
ans.pop()
dfs(Y,-1)
ans = ans[::-1]
ans.pop()
print(*[i+1 for i in ans])

=======
Suggestion 8

def dfs(u, par):
    global ans
    ans.append(u)
    for v in edge[u]:
        if v != par:
            dfs(v, u)
            ans.append(u)
    return

n, x, y = map(int, input().split())
edge = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    edge[u].append(v)
    edge[v].append(u)
ans = []
dfs(x, -1)
print(*ans)

=======
Suggestion 9

def dfs(v):
    for i in range(len(edges[v])):
        if edges[v][i][0] == 0:
            edges[v][i][0] = 1
            dfs(edges[v][i][1])
            ans.append(edges[v][i][1])
            break

n,x,y = map(int,input().split())
edges = [[] for _ in range(n+1)]
for i in range(n-1):
    u,v = map(int,input().split())
    edges[u].append([0,v])
    edges[v].append([0,u])
ans = []
dfs(x)
ans.append(x)
ans.reverse()
dfs(y)
print(*ans)

=======
Suggestion 10

def dfs(node, prev, dist):
    global dists
    dists[node] = dist
    for n in graph[node]:
        if n != prev:
            dfs(n, node, dist+1)

n, x, y = map(int, input().split())
x, y = x-1, y-1
graph = [[] for _ in range(n)]
for _ in range(n-1):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    graph[u].append(v)
    graph[v].append(u)

dists = [0] * n
dfs(x, -1, 0)
print(dists[y])
