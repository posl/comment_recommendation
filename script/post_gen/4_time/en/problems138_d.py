Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    tree = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        tree[a-1].append(b-1)
    counter = [0] * N
    for _ in range(Q):
        p, x = map(int, input().split())
        counter[p-1] += x
    stack = [0]
    while stack:
        v = stack.pop()
        for u in tree[v]:
            counter[u] += counter[v]
            stack.append(u)
    print(*counter)

=======
Suggestion 2

def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue
        counter[u] += counter[v]
        dfs(u, v)

N, Q = map(int, input().split())
edges = [[] for _ in range(N)]
counter = [0] * N
for _ in range(N-1):
    a, b = map(int, input().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)
for _ in range(Q):
    p, x = map(int, input().split())
    counter[p-1] += x
dfs(0, -1)
print(*counter)

=======
Suggestion 3

def dfs(v, p):
  for u in g[v]:
    if u == p:
      continue
    c[u] += c[v]
    dfs(u, v)

n, q = map(int, input().split())
g = [[] for i in range(n)]
for i in range(n - 1):
  a, b = map(int, input().split())
  g[a - 1].append(b - 1)
  g[b - 1].append(a - 1)
c = [0] * n
for i in range(q):
  p, x = map(int, input().split())
  c[p - 1] += x
dfs(0, -1)
print(*c)

=======
Suggestion 4

def dfs(v,p):
    for u in g[v]:
        if u==p:
            continue
        cnt[u]+=cnt[v]
        dfs(u,v)

n,q=map(int,input().split())
g=[[] for _ in range(n)]
cnt=[0]*n
for _ in range(n-1):
    a,b=map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
for _ in range(q):
    p,x=map(int,input().split())
    cnt[p-1]+=x
dfs(0,-1)
print(*cnt)

=======
Suggestion 5

def dfs(v, p):
    for u in G[v]:
        if u == p: continue
        cnt[u] += cnt[v]
        dfs(u, v)
N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(lambda x: int(x)-1, input().split())
    G[a].append(b)
    G[b].append(a)
cnt = [0]*N
for _ in range(Q):
    p, x = map(int, input().split())
    cnt[p-1] += x
dfs(0, -1)
print(*cnt)

=======
Suggestion 6

def dfs(v,p):
    for u in edges[v]:
        if u == p:
            continue
        cnt[u] += cnt[v]
        dfs(u,v)

N,Q = map(int,input().split())
edges = [[] for _ in range(N)]
cnt = [0]*N
for _ in range(N-1):
    a,b = map(int,input().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)
for _ in range(Q):
    p,x = map(int,input().split())
    cnt[p-1] += x
dfs(0,-1)
print(*cnt)

=======
Suggestion 7

def dfs(v, p, d):
  for u in G[v]:
    if u == p: continue
    d[u] += d[v]
    dfs(u, v, d)

N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N-1):
  a, b = map(int, input().split())
  G[a-1].append(b-1)
  G[b-1].append(a-1)

d = [0] * N
for _ in range(Q):
  p, x = map(int, input().split())
  d[p-1] += x

dfs(0, -1, d)
print(*d)

=======
Suggestion 8

def dfs(v, p, d):
    global D
    D[v] = d
    for nv in G[v]:
        if nv == p:
            continue
        dfs(nv, v, d+1)

N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    G[a].append(b)
    G[b].append(a)

D = [0] * N
dfs(0, -1, 0)

cnt = [0] * N
for _ in range(Q):
    p, x = map(int, input().split())
    p = p-1
    cnt[p] += x

for i in range(N):
    cnt[i] += D[i]

print(*cnt)

=======
Suggestion 9

def dfs(v, p, c):
    global ans
    ans[v-1] += c
    for i in range(len(G[v])):
        if G[v][i] == p:
            continue
        dfs(G[v][i], v, c)

N, Q = map(int, input().split())
G = [[] for i in range(N+1)]
ans = [0] * N

for i in range(N-1):
    a,b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

for i in range(Q):
    p,x = map(int, input().split())
    dfs(p, -1, x)

print(*ans)

=======
Suggestion 10

def dfs(v, p, d):
    global depth
    depth[v] = d
    for i in graph[v]:
        if i == p:
            continue
        dfs(i, v, d + 1)

n, q = map(int, input().split())
graph = [[] for i in range(n + 1)]
depth = [0] * (n + 1)

for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1, 0, 0)

ans = [0] * (n + 1)

for i in range(q):
    p, x = map(int, input().split())
    ans[p] += x

for i in range(1, n + 1):
    print(ans[i])
