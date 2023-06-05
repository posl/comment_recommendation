Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def dfs(v):
  seen[v] = True
  for i in range(n):
    if not seen[i] and G[v][i] == 1:
      dfs(i)

n,m = map(int,input().split())
G = [[0]*n for i in range(n)]
for i in range(m):
  a,b = map(int,input().split())
  G[a-1][b-1] = G[b-1][a-1] = 1

seen = [False]*n
res = 0
for i in range(n):
  if not seen[i]:
    dfs(i)
    res += 1
print(res)

=======
Suggestion 2

def dfs(v):
    visited[v] = True
    for i in range(n):
        if not visited[i] and graph[v][i]:
            dfs(i)

n,m = map(int,input().split())
graph = [[False for i in range(n)] for j in range(n)]
visited = [False for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    graph[a-1][b-1] = True
    graph[b-1][a-1] = True
count = 0
for i in range(n):
    if not visited[i]:
        dfs(i)
        count += 1
print(count)

=======
Suggestion 3

def dfs(v):
    seen[v] = True

    for i in range(n):
        if not graph[v][i]:
            continue
        if seen[i]:
            continue
        dfs(i)

n, m = map(int, input().split())
graph = [[False] * n for _ in range(n)]

for i in range(m):
    u, v = map(int, input().split())
    graph[u - 1][v - 1] = graph[v - 1][u - 1] = True

seen = [False] * n
count = 0

for v in range(n):
    if seen[v]:
        continue
    dfs(v)
    count += 1

print(count)

=======
Suggestion 4

def dfs(G, v, seen):
    seen[v] = True

    for next_v in G[v]:
        if seen[next_v]:
            continue
        dfs(G, next_v, seen)

=======
Suggestion 5

def dfs(i):
    if not visited[i]:
        visited[i] = True
        for j in range(n):
            if G[i][j]:
                dfs(j)

n, m = map(int, input().split())
G = [[False]*n for i in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u][v] = G[v][u] = True
visited = [False]*n
ans = 0
for i in range(n):
    if not visited[i]:
        dfs(i)
        ans += 1
print(ans)

=======
Suggestion 6

def dfs(x):
    global n, m, g, seen
    seen[x] = True
    for i in range(n):
        if g[x][i] == 1 and seen[i] == False:
            dfs(i)

n, m = map(int, input().split())
g = [[0]*n for _ in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u][v] = g[v][u] = 1
seen = [False]*n
ans = 0
for i in range(n):
    if seen[i] == False:
        dfs(i)
        ans += 1
print(ans)

=======
Suggestion 7

def dfs(v):
    seen[v] = True
    for i in range(n):
        if graph[v][i] == 0:
            continue
        if seen[i]:
            continue
        dfs(i)

n, m = map(int, input().split())
graph = [[0 for i in range(n)] for i in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u][v] = 1
    graph[v][u] = 1
seen = [False for i in range(n)]
ans = 0
for i in range(n):
    if seen[i]:
        continue
    dfs(i)
    ans += 1
print(ans)

=======
Suggestion 8

def dfs(s):
    global u, v, n, used
    used[s] = True
    for i in range(n):
        if not used[i] and (u[i] == s or v[i] == s):
            dfs(i)

n, m = map(int, input().split())
u = [0] * m
v = [0] * m
used = [False] * n
for i in range(m):
    u[i], v[i] = map(int, input().split())
ans = 0
for i in range(n):
    if not used[i]:
        dfs(i)
        ans += 1
print(ans)

=======
Suggestion 9

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
visited = [False] * n
count = 0

for _ in range(m):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

for i in range(n):
    if not visited[i]:
        dfs(graph, i, visited)
        count += 1

print(count)
