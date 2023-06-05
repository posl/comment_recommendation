Synthesizing 10/10 solutions

=======
Suggestion 1

def dfs(v, p):
    c = 1
    for u in graph[v]:
        if u == p:
            continue
        if c == color[v]:
            c += 1
        color[u] = c
        c += 1
        dfs(u, v)
    k[0] = max(k[0], c - 1)

n = int(input())
graph = [[] for _ in range(n + 1)]
color = [0] * (n + 1)
k = [0]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
color[1] = 1
dfs(1, -1)
print(k[0])
for i in range(1, n):
    print(color[i + 1])

=======
Suggestion 2

def main():
    N = int(input())
    
    # 邻接表
    graph = [[] for _ in range(N)]
    for i in range(N - 1):
        a, b = map(int, input().split())
        graph[a - 1].append((b - 1, i))
        graph[b - 1].append((a - 1, i))
    
    # 求解
    color = [-1] * (N - 1)
    used = [False] * N
    used[0] = True
    k = 0
    stack = [(0, -1, 0)]
    while stack:
        v, p, c = stack.pop()
        k = max(k, c + 1)
        cnt = 0
        for u, i in graph[v]:
            if used[u]:
                continue
            cnt += 1
            if cnt == c:
                cnt += 1
            color[i] = cnt
            used[u] = True
            stack.append((u, v, cnt))
    print(k)
    for c in color:
        print(c)

=======
Suggestion 3

def dfs(v, p, c):
    global ans
    k = 1
    for u in G[v]:
        if u == p:
            continue
        if k == c:
            k += 1
        ans[u] = k
        k += 1
        dfs(u, v, ans[u])

N = int(input())
G = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

ans = [0] * N
dfs(0, -1, -1)
print(max(ans))
for i in range(N - 1):
    print(ans[i])

=======
Suggestion 4

def main():
    pass

=======
Suggestion 5

def dfs(v, p, c):
    global color
    global G
    color[c] += 1
    k = 1
    for i in G[v]:
        if i == p:
            continue
        if k == c:
            k += 1
        dfs(i, v, k)
        k += 1

N = int(input())
color = [0]*(N+1)
G = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
dfs(1, -1, 1)
print(max(color))
for i in range(N-1):
    print(color[i+1])

=======
Suggestion 6

def dfs(v, p, c):
    global color
    color[c] += 1
    for u in G[v]:
        if u == p:
            continue
        dfs(u, v, c)

=======
Suggestion 7

def dfs(v, p=-1):
    global color, G
    c = 1
    for u in G[v]:
        if u == p:
            continue
        if c == color[v]:
            c += 1
        color[u] = c
        dfs(u, v)
        c += 1

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    G[a].append(b)
    G[b].append(a)

color = [0] * N
color[0] = 1
dfs(0)

print(max(color))
for c in color:
    print(c)

=======
Suggestion 8

def dfs(v, p, k):
    global ans
    c = 1
    for i in range(len(G[v])):
        if G[v][i] == p:
            continue
        if c == k:
            c += 1
        ans[G[v][i]] = c
        dfs(G[v][i], v, c)
        c += 1

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

ans = [0] * N
dfs(0, -1, 0)
print(max(ans))
for i in range(N - 1):
    print(ans[i + 1])

=======
Suggestion 9

def dfs(v, p, c):
    global color
    color[c] = True
    result[v] = c
    for w in g[v]:
        if w == p:
            continue
        nc = 1
        while color[nc]:
            nc += 1
        dfs(w, v, nc)

n = int(input())
g = [[] for _ in range(n+1)]
color = [False] * (n+1)
result = [0] * (n+1)
for _ in range(n-1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

dfs(1, -1, 1)
print(max(result))
for i in range(1, n):
    print(result[i])

=======
Suggestion 10

def solve():
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n-1)]
    neighbors = [[] for _ in range(n+1)]
    for a, b in edges:
        neighbors[a].append(b)
        neighbors[b].append(a)

    colors = [0] * (n+1)
    max_color = 0
    for a, b in edges:
        neighbor_colors = [colors[x] for x in neighbors[a]]
        neighbor_colors += [colors[x] for x in neighbors[b]]
        neighbor_colors = set(neighbor_colors)
        for i in range(1, n+1):
            if i not in neighbor_colors:
                colors[a] = i
                colors[b] = i
                max_color = max(max_color, i)
                break

    print(max_color)
    for a, b in edges:
        print(colors[a])

solve()
