Synthesizing 10/10 solutions

=======
Suggestion 1

def dfs(v, color, G):
    color[v] = 1
    for i in G[v]:
        if color[i] == 0:
            dfs(i, color, G)
    color[v] = 2

=======
Suggestion 2

def dfs(x):
    visited[x] = True
    for i in range(1, N+1):
        if graph[x][i] == 1 and not visited[i]:
            dfs(i)

N, M = map(int, input().split())
graph = [[0]*(N+1) for _ in range(N+1)]
visited = [False]*(N+1)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1

ans = 0
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        ans += 1

print(ans)

=======
Suggestion 3

def dfs(v):
    seen[v] = True
    for i in range(n):
        if G[v][i] == 0 or seen[i]:
            continue
        dfs(i)

n,m = map(int,input().split())
G = [[0]*n for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    G[a-1][b-1] = G[b-1][a-1] = 1
seen = [False]*n
ans = 0
for i in range(n):
    if seen[i]:
        continue
    dfs(i)
    ans += 1
print(ans)

=======
Suggestion 4

def dfs(v):
    seen[v] = True
    for next_v in graph[v]:
        if seen[next_v]:
            continue
        dfs(next_v)

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

seen = [False] * N
count = 0
for v in range(N):
    if seen[v]:
        continue
    dfs(v)
    count += 1

print(count)

=======
Suggestion 5

def dfs(v, graph, seen):
    seen[v] = True
    for next_v in graph[v]:
        if seen[next_v]:
            continue
        dfs(next_v, graph, seen)

=======
Suggestion 6

def dfs(v):
    visited[v] = True
    for i in range(n):
        if not visited[i] and G[v][i]:
            dfs(i)

n, m = map(int, input().split())
G = [[False for i in range(n)] for j in range(n)]
for i in range(m):
    s, t = map(int, input().split())
    G[s-1][t-1] = G[t-1][s-1] = True
visited = [False for i in range(n)]
ans = 0
for i in range(n):
    if not visited[i]:
        dfs(i)
        ans += 1
print(ans)

=======
Suggestion 7

def dfs(v):
    seen[v] = True
    for i in range(n):
        if not seen[i] and g[v][i] == 1:
            dfs(i)

n, m = map(int, input().split())

g = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a-1][b-1] = g[b-1][a-1] = 1

seen = [False for _ in range(n)]
ans = 0
for i in range(n):
    if not seen[i]:
        dfs(i)
        ans += 1
print(ans)

=======
Suggestion 8

def dfs(v):
    global cnt
    global visited
    visited[v] = True
    for i in range(1, n+1):
        if visited[i] == False and G[v][i] == 1:
            dfs(i)

n, m = map(int, input().split())
G = [[0] * (n+1) for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    G[a][b] = 1
    G[b][a] = 1

cnt = 0
visited = [False] * (n+1)
for i in range(1, n+1):
    if visited[i] == False:
        dfs(i)
        cnt += 1

print(cnt)

=======
Suggestion 9

def dfs(v):
    visited[v] = True
    for i in range(1, n+1):
        if not visited[i] and g[v][i]:
            dfs(i)

n, m = map(int, input().split())
g = [[False]*(n+1) for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    g[u][v] = g[v][u] = True

visited = [False]*(n+1)
ans = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        ans += 1

print(ans)

=======
Suggestion 10

def dfs(graph, v, seen):
    seen[v] = True
    for next_v in graph[v]:
        if seen[next_v]:
            continue
        dfs(graph, next_v, seen)

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)
seen = [False] * N
count = 0
for v in range(N):
    if seen[v]:
        continue
    dfs(graph, v, seen)
    count += 1
print(count)
