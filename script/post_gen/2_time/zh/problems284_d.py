Synthesizing 10/10 solutions

=======
Suggestion 1

def dfs(u):
    global n
    global m
    global g
    global visited
    global flag
    visited[u] = True
    for i in range(n):
        if not visited[i] and g[u][i] == 1:
            dfs(i)
    flag = True

n, m = [int(i) for i in input().split()]
g = [[0 for i in range(n)] for j in range(n)]
for i in range(m):
    u, v = [int(i) for i in input().split()]
    g[u - 1][v - 1] = 1
    g[v - 1][u - 1] = 1
visited = [False for i in range(n)]
ans = 0
for i in range(n):
    if not visited[i]:
        flag = False
        dfs(i)
        if flag:
            ans += 1
print(ans)

=======
Suggestion 2

def dfs(v):
    seen[v] = True

    for next_v in graph[v]:
        if seen[next_v]:
            continue
        dfs(next_v)

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

seen = [False] * n

count = 0
for v in range(n):
    if seen[v]:
        continue

    dfs(v)
    count += 1

print(count)

=======
Suggestion 3

def dfs(v):
    seen[v] = True
    for i in range(n):
        if not g[v][i]:
            continue
        if seen[i]:
            continue
        dfs(i)

n,m = map(int,input().split())
g = [[False]*n for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    g[a-1][b-1] = g[b-1][a-1] = True
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
    group[v] = cnt
    for i in range(n):
        if not seen[i] and g[v][i] == 1:
            dfs(i)


n, m = map(int, input().split())
g = [[0] * n for i in range(n)]
seen = [False] * n
group = [None] * n
cnt = 0

for i in range(m):
    u, v = map(int, input().split())
    g[u - 1][v - 1] = 1
    g[v - 1][u - 1] = 1

for i in range(n):
    if not seen[i]:
        cnt += 1
        dfs(i)

print(cnt)

=======
Suggestion 5

def dfs(v):
    seen[v] = True
    for i in range(n):
        if not G[v][i]:
            continue
        if seen[i]:
            continue
        dfs(i)

n,m = map(int,input().split())
G = [[False]*n for i in range(n)]
for i in range(m):
    u,v = map(int,input().split())
    u -= 1
    v -= 1
    G[u][v] = G[v][u] = True

seen = [False]*n
res = 0
for v in range(n):
    if seen[v]:
        continue
    dfs(v)
    res += 1
print(res)

=======
Suggestion 6

def dfs(v):
    seen[v] = True
    for i in range(n):
        if not seen[i] and G[v][i] == 1:
            dfs(i)

n, m = map(int, input().split())
G = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    G[a-1][b-1] = G[b-1][a-1] = 1

seen = [False for _ in range(n)]
res = 0
for i in range(n):
    if not seen[i]:
        dfs(i)
        res += 1
print(res)

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
    return

n,m = map(int,input().split())
graph = [[0 for i in range(n)] for j in range(n)]
seen = [False for i in range(n)]
for i in range(m):
    u,v = map(int,input().split())
    graph[u-1][v-1] = 1
    graph[v-1][u-1] = 1
ans = 0
for i in range(n):
    if seen[i]:
        continue
    dfs(i)
    ans += 1
print(ans)

=======
Suggestion 8

def dfs(v):
    seen[v] = True
    for i in range(n):
        if not seen[i] and G[v][i] == 1:
            dfs(i)

n, m = map(int, input().split())
G = [[0] * n for _ in range(n)]
seen = [False] * n

for i in range(m):
    u, v = map(int, input().split())
    G[u - 1][v - 1] = G[v - 1][u - 1] = 1

ans = 0
for i in range(n):
    if not seen[i]:
        dfs(i)
        ans += 1

print(ans)

=======
Suggestion 9

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
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

seen = [False] * N
count = 0
for v in range(N):
    if seen[v]:
        continue
    dfs(v)
    count += 1

print(count)

=======
Suggestion 10

def dfs(i):
    visited[i] = 1
    for j in range(n):
        if visited[j] == 0 and G[i][j] == 1:
            dfs(j)

n, m = map(int, input().split())
G = [[0 for i in range(n)] for j in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    G[a-1][b-1] = 1
    G[b-1][a-1] = 1
visited = [0 for i in range(n)]
ans = 0
for i in range(n):
    if visited[i] == 0:
        dfs(i)
        ans += 1
print(ans)
