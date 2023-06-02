Synthesizing 10/10 solutions

=======
Suggestion 1

def dfs(v, p, c):
    color = 1
    for i in range(len(g[v])):
        if g[v][i] == p:
            continue
        if color == c:
            color += 1
        ans[i] = color
        dfs(g[v][i], v, color)
        color += 1

n = int(input())
g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

ans = [0] * (n - 1)
dfs(0, -1, -1)
print(max(ans))
for i in range(n - 1):
    print(ans[i])

=======
Suggestion 2

def dfs1(G, v, p, d, c):
    c[v] = d
    for u in G[v]:
        if u == p:
            continue
        dfs1(G, u, v, d + 1, c)

=======
Suggestion 3

def dfs(v, p, c):
    color[c] = True
    ans[v] = c
    for u in G[v]:
        if u == p:
            continue
        c += 1
        if c == ans[p]:
            c += 1
        dfs(u, v, c)
        c += 1

N = int(input())
G = [[] for i in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

ans = [0] * N
color = [False] * N
dfs(0, -1, 1)
print(max(ans))
for i in range(N-1):
    print(ans[i])

=======
Suggestion 4

def dfs(v, p):
    global k
    c = 0
    for u in g[v]:
        if u == p:
            continue
        c += 1
        if c == c2:
            c += 1
        k = max(k, c)
        color[(v, u)] = c
        dfs(u, v)

n = int(input())
g = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

k = 0
color = {}
for v in range(n):
    k = max(k, len(g[v]))
    if k == len(g[v]):
        c1 = v
    if k == len(g[v]) - 1:
        c2 = v

dfs(c1, -1)

print(k)
for i in range(n - 1):
    print(color[(i, i + 1)])

=======
Suggestion 5

def dfs(v, p, c):
    color = 1
    for u in G[v]:
        if u == p:
            continue
        if color == c:
            color += 1
        ans[u] = color
        dfs(u, v, color)
        color += 1

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

ans = [0] * N
ans[0] = 1
dfs(0, -1, 1)
print(max(ans))
for i in range(N - 1):
    print(ans[i + 1])

=======
Suggestion 6

def dfs(i, c):
    global color
    color[i] = c
    for j in adj[i]:
        if color[j] == 0:
            dfs(j, c)

n = int(input())
color = [0] * (n + 1)
adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

dfs(1, 1)
print(max(color))
for i in range(1, n):
    print(color[i])

=======
Suggestion 7

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n-1):
        a0, b0 = map(int, input().split())
        a.append(a0)
        b.append(b0)

    c = [0 for i in range(n)]
    for i in range(n-1):
        c0 = c[a[i]-1]
        if c0 == 0:
            c0 = c[b[i]-1]
        elif c0 == c[b[i]-1]:
            c0 += 1
        c[a[i]-1] = c0
        c[b[i]-1] = c0
    print(max(c))
    for i in range(n-1):
        print(c[a[i]-1])

=======
Suggestion 8

def main():
    N = int(input())
    edges = []
    for i in range(N-1):
        a, b = map(int, input().split())
        edges.append([a, b])
    edges.sort()
    color = [0] * (N+1)
    for i in range(N-1):
        a, b = edges[i][0], edges[i][1]
        if color[a] == 0 and color[b] == 0:
            color[a] = 1
            color[b] = 2
        elif color[a] == 0:
            if color[b] == 1:
                color[a] = 2
            else:
                color[a] = 1
        elif color[b] == 0:
            if color[a] == 1:
                color[b] = 2
            else:
                color[b] = 1
        else:
            pass
    print(max(color))
    for i in range(N-1):
        print(color[edges[i][0]])

=======
Suggestion 9

def main():
    n = int(input())
    edges = []
    for i in range(n-1):
        a,b = (int(x) for x in input().split())
        edges.append((a,b))
    edges.sort()
    colors = {}
    for a,b in edges:
        if a not in colors:
            colors[a] = 1
        if b not in colors:
            colors[b] = colors[a] + 1
        else:
            colors[b] = max(colors[b],colors[a]+1)
    print(max(colors.values()))
    for a,b in edges:
        print(colors[b])

=======
Suggestion 10

def dfs(v, p, c):
    color[c] = True
    col[v] = c
    for u in G[v]:
        if u == p:
            continue
        c += 1
        while color[c]:
            c += 1
        dfs(u, v, c)
        c -= 1

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

col = [0] * N
color = [False] * N
dfs(0, -1, 0)
print(max(col))

for i in range(N - 1):
    print(col[i] + 1)
