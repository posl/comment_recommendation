Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,x,y = map(int,input().split())
    u = [0]*(n-1)
    v = [0]*(n-1)
    for i in range(n-1):
        u[i],v[i] = map(int,input().split())
    for i in range(n-1):
        if u[i] == x and v[i] == y:
            print(i+1)
        elif u[i] == y and v[i] == x:
            print(i+1)
        else:
            pass

=======
Suggestion 2

def main():
    n,x,y = map(int, input().split())
    u = [0] * (n-1)
    v = [0] * (n-1)
    for i in range(n-1):
        u[i],v[i] = map(int, input().split())
    #print(n,x,y,u,v)
    ans = []
    for i in range(n-1):
        for j in range(i+1,n):
            #print(i,j)
            if i == x-1 and j == y-1:
                ans.append(i+1)
                ans.append(j+1)
                continue
            if i == y-1 and j == x-1:
                ans.append(i+1)
                ans.append(j+1)
                continue
            if i == j:
                continue
            if i == x-1:
                if j in v:
                    ans.append(i+1)
                    ans.append(j+1)
                    continue
            if i == y-1:
                if j in v:
                    ans.append(i+1)
                    ans.append(j+1)
                    continue
            if j == x-1:
                if i in v:
                    ans.append(i+1)
                    ans.append(j+1)
                    continue
            if j == y-1:
                if i in v:
                    ans.append(i+1)
                    ans.append(j+1)
                    continue
            if u[i] == u[j]:
                ans.append(u[i])
                ans.append(v[i])
                ans.append(v[j])
                continue
            if u[i] == v[j]:
                ans.append(u[i])
                ans.append(v[i])
                ans.append(u[j])
                continue
            if v[i] == u[j]:
                ans.append(v[i])
                ans.append(u[i])
                ans.append(v[j])
                continue
            if v[i] == v[j]:
                ans.append(v[i])
                ans.append(u[i])
                ans.append(u[j])
                continue
    #print(ans)
    print(*ans)

=======
Suggestion 3

def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    graph = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)

    dist = [-1]*N
    dist[X] = 0
    q = [X]
    while q:
        x = q.pop()
        for y in graph[x]:
            if dist[y] == -1:
                dist[y] = dist[x] + 1
                q.append(y)

    count = [0]*N
    count[0] = N*(N-1)//2
    for d in dist:
        if d != -1:
            count[d] += 1

    print(count[Y])

=======
Suggestion 4

def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    edges = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        edges[a].append(b)
        edges[b].append(a)
    dist = [N] * N
    dist[X] = 0
    queue = [X]
    while queue:
        v = queue.pop(0)
        for w in edges[v]:
            if dist[w] > dist[v] + 1:
                dist[w] = dist[v] + 1
                queue.append(w)
    print(dist[Y])

=======
Suggestion 5

def dfs(G, v):
    seen[v] = True
    order.append(v)
    for next_v in G[v]:
        if seen[next_v]: continue
        dfs(G, next_v)
        order.append(v)

N, X, Y = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

seen = [False] * N
order = []
dfs(G, X-1)
print(order)

=======
Suggestion 6

def dfs(v, p, g, d):
    for u in g[v]:
        if u == p:
            continue
        d[u] = d[v] + 1
        dfs(u, v, g, d)

=======
Suggestion 7

def dfs(v, p):
    for u in g[v]:
        if u == p:
            continue
        d[u] = v
        dfs(u, v)

n, x, y = map(int, input().split())
g = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

d = [0] * (n + 1)
dfs(x, -1)

ans = [y]
while y != x:
    y = d[y]
    ans.append(y)

print(*ans[::-1])

=======
Suggestion 8

def bfs(G, s):
    N = len(G)
    dist = [-1]*N
    dist[s] = 0
    q = [s]
    while q:
        u = q.pop(0)
        for v in G[u]:
            if dist[v] == -1:
                dist[v] = dist[u]+1
                q.append(v)
    return dist

=======
Suggestion 9

def dfs(start, end, g):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in g[vertex] - set(path):
            if next == end:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

N, X, Y = map(int, input().split())
g = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
print(len(list(dfs(X, Y, g))[0]) - 1)

=======
Suggestion 10

def dfs(v, p):
    global dep
    dep[v] = dep[p]+1
    for u in g[v]:
        if u == p:
            continue
        dfs(u, v)

n, x, y = map(int, input().split())
x -= 1
y -= 1
g = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
dep = [0]*n
dfs(x, x)
print(dep[y]-1)
