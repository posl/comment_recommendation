Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, q = map(int, input().split())
    a = [0] * n
    for i in range(n - 1):
        x, y = map(int, input().split())
        a[x - 1] += 1
        a[y - 1] += 1
    for i in range(q):
        x, y = map(int, input().split())
        a[x - 1] += y
    print(*a)

=======
Suggestion 2

def main():
    n,q = map(int, input().split())
    nodes = [[] for _ in range(n)]
    for i in range(n-1):
        a,b = map(int, input().split())
        nodes[a-1].append(b-1)
        nodes[b-1].append(a-1)
    values = [0]*n
    for i in range(q):
        p,x = map(int, input().split())
        values[p-1] += x
    stack = [0]
    visited = [False]*n
    visited[0] = True
    while len(stack) > 0:
        parent = stack.pop()
        for child in nodes[parent]:
            if not visited[child]:
                values[child] += values[parent]
                visited[child] = True
                stack.append(child)
    print(' '.join(map(str, values)))

=======
Suggestion 3

def dfs(v, p):
    for i in g[v]:
        if i != p:
            c[i] += c[v]
            dfs(i, v)

n, q = map(int, input().split())
g = [[] for i in range(n)]
c = [0] * n
for i in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
for i in range(q):
    p, x = map(int, input().split())
    c[p - 1] += x
dfs(0, -1)
print(*c)

=======
Suggestion 4

def dfs(v,p):
    for u in to[v]:
        if u == p:
            continue
        counter[u] += counter[v]
        dfs(u,v)

n,q = map(int,input().split())
to = [[] for _ in range(n)]
counter = [0]*n
for _ in range(n-1):
    a,b = map(int,input().split())
    to[a-1].append(b-1)
    to[b-1].append(a-1)
for _ in range(q):
    p,x = map(int,input().split())
    counter[p-1] += x
dfs(0,-1)
print(*counter)

=======
Suggestion 5

def dfs(v, p, x):
    for u in g[v]:
        if u == p:
            continue
        c[u] += x
        dfs(u, v, x)

N, Q = map(int, input().split())
g = [[] for _ in range(N)]
c = [0] * N
for _ in range(N - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
for _ in range(Q):
    p, x = map(int, input().split())
    c[p - 1] += x
dfs(0, -1, 0)
print(*c)

=======
Suggestion 6

def dfs(v, p, d):
    global depth
    depth[v] = d
    for u in g[v]:
        if u == p:
            continue
        dfs(u, v, d + 1)

n, q = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
depth = [0] * n
dfs(0, -1, 0)
cnt = [0] * n
for _ in range(q):
    p, x = map(int, input().split())
    cnt[p - 1] += x
for i in range(n):
    print(cnt[i] + depth[i], end=" ")

=======
Suggestion 7

def dfs(node, parent, counters, edges):
    counters[node] += counters[parent]
    for child in edges[node]:
        if child == parent:
            continue
        dfs(child, node, counters, edges)

=======
Suggestion 8

def dfs(v, p, d):
    global D
    D[v] = d
    for nv in G[v]:
        if nv == p:
            continue
        dfs(nv, v, d+1)

=======
Suggestion 9

def dfs(v, p, d):
    for u in g[v]:
        if u == p:
            continue
        dfs(u, v, d + c[u])
    print(d, end=" ")

n, q = map(int, input().split())
g = [[] for i in range(n)]
c = [0] * n
for i in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
for i in range(q):
    p, x = map(int, input().split())
    c[p - 1] += x
dfs(0, -1, c[0])

=======
Suggestion 10

def add_to_tree(tree, parent, child, value):
    if parent in tree:
        tree[parent].append((child, value))
    else:
        tree[parent] = [(child, value)]
