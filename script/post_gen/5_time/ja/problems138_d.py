Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
    counter = [0] * N
    for _ in range(Q):
        p, x = map(int, input().split())
        counter[p - 1] += x
    stack = [0]
    while stack:
        node = stack.pop()
        for child in graph[node]:
            counter[child] += counter[node]
            stack.append(child)
    print(*counter)

=======
Suggestion 2

def dfs(v, p, d):
    for i in G[v]:
        if i != p:
            d[i] += d[v]
            dfs(i, v, d)

N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

d = [0] * N
for _ in range(Q):
    p, x = map(int, input().split())
    d[p - 1] += x

dfs(0, -1, d)
print(*d)

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    #print(N, Q)
    #N = 4
    #Q = 3
    #N = 6
    #Q = 2
    edges = []
    for i in range(N-1):
        a, b = map(int, input().split())
        #a, b = map(int, input().split())
        #a, b = i+1, i+2
        edges.append((a, b))
    #print(edges)
    #edges = [(1, 2), (2, 3), (2, 4)]
    #edges = [(1, 2), (1, 3), (2, 4), (3, 6), (2, 5)]
    #edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
    #edges = [(1, 2), (2, 3), (3, 4), (4, 5)]
    #edges = [(1, 2), (2, 3), (3, 4)]
    #edges = [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6)]
    #edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6)]
    #edges = [(1, 2), (1, 3), (1, 4), (1, 5)]
    #edges = [(1, 2), (2, 3), (3, 4)]
    #edges = [(1, 2), (1, 3), (2, 4), (3, 5), (3, 6)]
    #edges = [(1, 2), (2, 3), (3, 4), (4, 5)]
    #edges = [(1, 2), (1, 3), (2, 4), (3, 5), (4, 6)]
    #edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5,

=======
Suggestion 4

def main():
    n, q = map(int, input().split())
    edges = []
    for i in range(n-1):
        edges.append(list(map(int, input().split())))
    px = []
    for i in range(q):
        px.append(list(map(int, input().split())))

    counter = [0] * n
    for p, x in px:
        counter[p-1] += x

    counter2 = [0] * (n+1)
    for i in range(n-1):
        a, b = edges[i]
        counter2[a] += counter[b-1]
        counter2[b] += counter[a-1]

    counter2 = counter2[1:]
    counter = [counter[i] + counter2[i] for i in range(n)]
    print(*counter)

=======
Suggestion 5

def dfs(v, p, d):
    for nv in g[v]:
        if nv == p:
            continue
        depth[nv] = d + 1
        dfs(nv, v, d + 1)

N, Q = map(int, input().split())
g = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
depth = [0] * N
dfs(0, -1, 0)
for _ in range(Q):
    p, x = map(int, input().split())
    p -= 1
    print(depth[p] + x)

=======
Suggestion 6

def main():
    n,q = map(int,input().split())
    a = [0 for i in range(n+1)]
    for i in range(n-1):
        x,y = map(int,input().split())
        a[x] += 1
        a[y] += 1
    b = [0 for i in range(n+1)]
    for i in range(q):
        x,y = map(int,input().split())
        b[x] += y
    for i in range(1,n+1):
        print(a[i]+b[i],end=" ")
    print()

=======
Suggestion 7

def main():
    N, Q = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(N-1)]
    queries = [list(map(int, input().split())) for _ in range(Q)]

    # 一つの頂点に対して、その頂点の値と、その頂点の子頂点の値を管理する
    values = [0] * N
    childs = [[] for _ in range(N)]

    for i in range(N-1):
        a, b = edges[i]
        childs[a-1].append(b-1)

    for i in range(Q):
        p, x = queries[i]
        values[p-1] += x

    # 親から子に値を伝播させる
    stack = [0]
    while stack:
        v = stack.pop()
        for c in childs[v]:
            values[c] += values[v]
            stack.append(c)

    print(*values)

=======
Suggestion 8

def main():
    N, Q = map(int, input().split())
    tree = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        tree[a].append(b)
    tree[1].append(1)
    point = [0] * (N+1)
    for _ in range(Q):
        p, x = map(int, input().split())
        point[p] += x
    ans = [0] * (N+1)
    ans[1] = point[1]
    for i in range(2, N+1):
        ans[i] = ans[i-1] + point[i]
    for i in range(1, N+1):
        print(ans[i], end=" ")

=======
Suggestion 9

def main():
    N, Q = map(int, input().split())
    edge = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        edge[a-1].append(b-1)
        edge[b-1].append(a-1)
    counter = [0] * N
    for _ in range(Q):
        p, x = map(int, input().split())
        counter[p-1] += x
    stack = [0]
    visited = [False] * N
    visited[0] = True
    while stack:
        v = stack.pop()
        for e in edge[v]:
            if visited[e]:
                continue
            counter[e] += counter[v]
            visited[e] = True
            stack.append(e)
    print(*counter)

=======
Suggestion 10

def dfs(now, prev):
    for i in edge[now]:
        if i == prev:
            continue
        counter[i] += counter[now]
        dfs(i, now)

N, Q = map(int, input().split())
edge = [[] for _ in range(N)]
counter = [0 for _ in range(N)]

for i in range(N-1):
    a, b = map(int, input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)

for i in range(Q):
    p, x = map(int, input().split())
    counter[p-1] += x

dfs(0, -1)

for i in counter:
    print(i, end=" ")
