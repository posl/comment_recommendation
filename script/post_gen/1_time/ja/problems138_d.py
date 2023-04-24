Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    counter = [0] * N
    for _ in range(Q):
        p, x = map(int, input().split())
        counter[p-1] += x
    visited = [False] * N
    stack = [(0, 0)]
    visited[0] = True
    while stack:
        v, p = stack.pop()
        counter[v] += p
        for w in G[v]:
            if visited[w]:
                continue
            stack.append((w, counter[v]))
            visited[w] = True
    print(*counter)

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        G[a - 1].append(b - 1)
    P = []
    X = []
    for _ in range(Q):
        p, x = map(int, input().split())
        P.append(p - 1)
        X.append(x)
    ans = [0] * N
    for i in range(Q):
        ans[P[i]] += X[i]
    stack = [0]
    while stack:
        u = stack.pop()
        for v in G[u]:
            ans[v] += ans[u]
            stack.append(v)
    print(*ans)

=======
Suggestion 3

def dfs(v, p=-1):
    for nv in g[v]:
        if nv == p:
            continue
        cnt[nv] += cnt[v]
        dfs(nv, v)

n, q = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
cnt = [0]*n
for _ in range(q):
    p, x = map(int, input().split())
    cnt[p-1] += x
dfs(0)
print(*cnt)

=======
Suggestion 4

def dfs(v, p):
    for u in G[v]:
        if u == p:
            continue
        C[u] += C[v]
        dfs(u, v)

N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

C = [0] * N
for _ in range(Q):
    p, x = map(int, input().split())
    C[p - 1] += x

dfs(0, -1)
print(*C)

=======
Suggestion 5

def main():
    #入力
    n,q = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(n-1)]
    px = [list(map(int,input().split())) for _ in range(q)]

    #隣接リストを作成
    graph = [[] for _ in range(n+1)]
    for a,b in ab:
        graph[a].append(b)
        graph[b].append(a)

    #累積和
    val = [0]*(n+1)
    for p,x in px:
        val[p] += x

    #DFS
    queue = [1]
    seen = [False]*(n+1)
    seen[1] = True
    while queue:
        v = queue.pop()
        for i in graph[v]:
            if seen[i]:
                continue
            val[i] += val[v]
            seen[i] = True
            queue.append(i)

    #出力
    print(*val[1:])

=======
Suggestion 6

def dfs(v, p, c):
    ans[v] += c
    for u in g[v]:
        if u == p:
            continue
        dfs(u, v, ans[v])

n, q = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
ans = [0] * n
for _ in range(q):
    p, x = map(int, input().split())
    ans[p-1] += x
dfs(0, -1, 0)
print(*ans)

=======
Suggestion 7

def main():
    n, q = map(int, input().split())
    n -= 1
    edge = [[] for _ in range(n)]
    for _ in range(n):
        a, b = map(int, input().split())
        edge[a-1].append(b-1)
        edge[b-1].append(a-1)
    cnt = [0] * n
    for _ in range(q):
        p, x = map(int, input().split())
        cnt[p-1] += x
    stack = [0]
    while stack:
        v = stack.pop()
        for u in edge[v]:
            if u == 0:
                continue
            cnt[u-1] += cnt[v]
            stack.append(u)
    print(*cnt)

main()

=======
Suggestion 8

def dfs(v, p, d):
    dist[v] = d
    for u in G[v]:
        if u == p:
            continue
        dfs(u, v, d + 1)

N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
dist = [0] * N
dfs(0, -1, 0)
ans = [0] * N
for _ in range(Q):
    p, x = map(int, input().split())
    p -= 1
    ans[p] += x
for i in range(N):
    print(ans[i] + dist[i])

=======
Suggestion 9

def dfs(v, p, d):
    dist[v] = d
    for nv in g[v]:
        if nv == p: continue
        dfs(nv, v, d + 1)

n, q = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    g[a].append(b)
    g[b].append(a)

dist = [0] * n
dfs(0, -1, 0)

for _ in range(q):
    p, x = map(int, input().split())
    p = p - 1
    print(dist[p] + x)

=======
Suggestion 10

def dfs(v, p, x):
    for nv in G[v]:
        if nv == p: continue
        cnt[nv] += x
        dfs(nv, v, x)

N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    G[a].append(b)
    G[b].append(a)

cnt = [0] * N
for _ in range(Q):
    p, x = map(int, input().split())
    p -= 1
    cnt[p] += x

dfs(0, -1, 0)
print(*cnt)
