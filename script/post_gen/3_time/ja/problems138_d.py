Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,q = map(int,input().split())
    g = [[] for _ in range(n)]
    for _ in range(n-1):
        a,b = map(int,input().split())
        g[a-1].append(b-1)
        g[b-1].append(a-1)
    counter = [0]*n
    for _ in range(q):
        p,x = map(int,input().split())
        counter[p-1] += x
    ans = [0]*n
    def dfs(v,p=-1):
        ans[v] = counter[v]
        for to in g[v]:
            if to == p:
                continue
            counter[to] += counter[v]
            dfs(to,v)
    dfs(0)
    print(*ans)

=======
Suggestion 2

def main():
    n, q = map(int, input().split())
    a = [0] * (n + 1)
    for i in range(n - 1):
        x, y = map(int, input().split())
        a[x] += 1
        a[y] += 1
    b = [0] * (n + 1)
    for i in range(q):
        x, y = map(int, input().split())
        b[x] += y

    for i in range(1, n + 1):
        print(a[i] + b[i], end=' ')

=======
Suggestion 3

def main():
    n, q = map(int, input().split())

    tree = [[] for _ in range(n)]

    for i in range(n-1):
        a, b = map(int, input().split())
        tree[a-1].append(b-1)
        tree[b-1].append(a-1)

    counter = [0] * n

    for i in range(q):
        p, x = map(int, input().split())
        counter[p-1] += x

    visited = [False] * n
    visited[0] = True

    stack = [0]

    while stack:
        v = stack.pop()
        visited[v] = True

        for i in tree[v]:
            if visited[i]:
                continue
            counter[i] += counter[v]
            stack.append(i)

    print(' '.join(map(str, counter)))

=======
Suggestion 4

def dfs(v, p=-1):
    for nv in G[v]:
        if nv == p:
            continue
        ans[nv] += ans[v]
        dfs(nv, v)

N, Q = map(int, input().split())
G = [[] for _ in range(N)]
ans = [0] * N
for _ in range(N-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
for _ in range(Q):
    p, x = map(int, input().split())
    ans[p-1] += x
dfs(0)
print(*ans)

=======
Suggestion 5

def dfs(now, prev):
    for next in edge[now]:
        if next == prev:
            continue
        counter[next] += counter[now]
        dfs(next, now)

N, Q = map(int, input().split())
edge = [[] for _ in range(N)]
counter = [0] * N
for i in range(N-1):
    a, b = map(int, input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)
for i in range(Q):
    p, x = map(int, input().split())
    counter[p-1] += x
dfs(0, -1)
print(*counter)

=======
Suggestion 6

def main():
    import sys
    input = sys.stdin.readline

    from collections import deque

    N, Q = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
    counter = [0] * (N + 1)
    for _ in range(Q):
        p, x = map(int, input().split())
        counter[p] += x
    queue = deque([1])
    while queue:
        node = queue.pop()
        for child in graph[node]:
            counter[child] += counter[node]
            queue.append(child)
    print(*counter[1:])

=======
Suggestion 7

def dfs(v, p, d, c):
    c[v] += d
    for i in g[v]:
        if i == p:
            continue
        dfs(i, v, d, c)

n, q = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
c = [0] * n
for i in range(q):
    p, x = map(int, input().split())
    p -= 1
    dfs(p, -1, x, c)
print(*c)

=======
Suggestion 8

def dfs(v, p, d):
    for i in G[v]:
        if i != p:
            D[i] += d
            dfs(i, v, D[i])

N, Q = map(int, input().split())
G = [[] for _ in range(N)]
D = [0] * N
for i in range(N-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
for i in range(Q):
    p, x = map(int, input().split())
    D[p-1] += x
dfs(0, -1, 0)
print(*D)

=======
Suggestion 9

def dfs(v, p, c):
    global ans
    ans[v] += c
    for next_v in graph[v]:
        if next_v == p:
            continue
        dfs(next_v, v, ans[v])

n, q = map(int, input().split())
graph = [[] for _ in range(n)]
ans = [0 for _ in range(n)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

for _ in range(q):
    p, x = map(int, input().split())
    ans[p-1] += x

dfs(0, -1, 0)

print(*ans)

=======
Suggestion 10

def dfs(v, p, d):
    depth[v] = d
    for u in tree[v]:
        if u == p:
            continue
        dfs(u, v, d + 1)
