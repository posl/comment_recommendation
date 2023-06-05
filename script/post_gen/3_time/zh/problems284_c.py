Synthesizing 10/10 solutions

=======
Suggestion 1

def dfs(v):
    seen[v] = True
    for i in range(n):
        if G[v][i] == 1 and seen[i] == False:
            dfs(i)

n, m = map(int, input().split())
G = [[0 for i in range(n)] for j in range(n)]
seen = [False for i in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    G[u-1][v-1] = 1
    G[v-1][u-1] = 1
ans = 0
for i in range(n):
    if seen[i] == False:
        dfs(i)
        ans += 1
print(ans)

=======
Suggestion 2

def dfs(i):
    visited[i]=True
    for j in range(n):
        if visited[j]==False and G[i][j]:
            dfs(j)

n,m=map(int,input().split())
G=[[False]*n for i in range(n)]
for i in range(m):
    u,v=map(int,input().split())
    u-=1
    v-=1
    G[u][v]=G[v][u]=True

visited=[False]*n
ans=0
for i in range(n):
    if visited[i]==False:
        dfs(i)
        ans+=1

print(ans)

=======
Suggestion 3

def dfs(v, c):
    seen[v] = c
    for vv in graph[v]:
        if seen[vv]:
            continue
        dfs(vv, c)

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

seen = [0] * N
c = 0
for v in range(N):
    if seen[v]:
        continue
    c += 1
    dfs(v, c)

print(c)

=======
Suggestion 4

def dfs(v):
    global n, m, g, seen
    seen[v] = True
    for i in range(n):
        if g[v][i] == 1 and seen[i] == False:
            dfs(i)

n, m = map(int, input().split())
g = [[0]*n for i in range(n)]
seen = [False]*n
for i in range(m):
    a, b = map(int, input().split())
    g[a-1][b-1] = 1
    g[b-1][a-1] = 1

ans = 0
for i in range(n):
    if seen[i] == False:
        dfs(i)
        ans += 1

print(ans)

=======
Suggestion 5

def dfs(v):
    visited[v] = True
    for i in range(n):
        if G[v][i] and not visited[i]:
            dfs(i)

n, m = map(int, input().split())
G = [[False for _ in range(n)] for _ in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    G[u-1][v-1] = G[v-1][u-1] = True
visited = [False] * n
cnt = 0
for i in range(n):
    if not visited[i]:
        dfs(i)
        cnt += 1
print(cnt)

=======
Suggestion 6

def dfs(now, last):
    if last != -1:
        visited[now] = True
    for i in range(n):
        if not visited[i] and graph[now][i]:
            dfs(i, now)

n, m = map(int, input().split())
graph = [[False] * n for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u - 1][v - 1] = graph[v - 1][u - 1] = True
visited = [False] * n
count = 0
for i in range(n):
    if not visited[i]:
        dfs(i, -1)
        count += 1
print(count)

=======
Suggestion 7

def dfs(v):
    seen[v] = True
    for next_v in graph[v]:
        if seen[next_v]:
            continue
        dfs(next_v)

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

seen = [False] * n
count = 0
for v in range(n):
    if seen[v]:
        continue
    dfs(v)
    count += 1

print(count)

=======
Suggestion 8

def dfs(v):
    seen[v] = True

    for i in range(n):
        if graph[v][i] == 0:
            continue
        if seen[i]:
            continue
        dfs(i)

n, m = map(int, input().split())

graph = [[0] * n for _ in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u][v] = 1
    graph[v][u] = 1

ans = 0
seen = [False] * n
for v in range(n):
    if seen[v]:
        continue
    dfs(v)
    ans += 1

print(ans)

=======
Suggestion 9

def dfs(u):
    global visited
    visited[u] = True
    for v in range(n):
        if not visited[v] and G[u][v]:
            dfs(v)

n, m = map(int, input().split())
G = [[False] * n for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    G[u-1][v-1] = G[v-1][u-1] = True
visited = [False] * n
ans = 0
for u in range(n):
    if not visited[u]:
        dfs(u)
        ans += 1
print(ans)

=======
Suggestion 10

def dfs(v):
    global seen,graph
    seen[v] = True
    for next_v in graph[v]:
        if seen[next_v]:
            continue
        dfs(next_v)
