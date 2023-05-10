Synthesizing 10/10 solutions

=======
Suggestion 1

def dfs(v, c):
    color[v] = c
    for next_v, w in graph[v]:
        if color[next_v] != -1:
            continue
        if w % 2 == 0:
            dfs(next_v, c)
        else:
            dfs(next_v, 1 - c)

N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append((v, w))
    graph[v].append((u, w))

color = [-1] * N
dfs(0, 0)
for c in color:
    print(c)

=======
Suggestion 2

def main():
    N = int(input())
    v = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, w, c = map(int, input().split())
        v[u - 1].append((w - 1, c))
        v[w - 1].append((u - 1, c))

    q = [0]
    color = [-1] * N
    color[0] = 0
    while q:
        p = q.pop()
        for w, c in v[p]:
            if color[w] == -1:
                color[w] = color[p] ^ c
                q.append(w)
    print(*color, sep="\n")

=======
Suggestion 3

def dfs(s, c):
    color[s] = c
    for i in range(len(G[s])):
        if color[G[s][i]] == 0:
            dfs(G[s][i], -c)

N = int(input())
G = [[] for i in range(N)]
color = [0] * N

for i in range(N - 1):
    u, v, w = map(int, input().split())
    G[u - 1].append(v - 1)
    G[v - 1].append(u - 1)

dfs(0, 1)
for i in range(N):
    if color[i] == 1:
        print(0)
    else:
        print(1)

=======
Suggestion 4

def main():
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n-1)]
    ans = [0] * n
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u-1].append((v-1, w))
        graph[v-1].append((u-1, w))
    def dfs(v, p, d):
        ans[v] = d % 2
        for u, w in graph[v]:
            if u == p:
                continue
            dfs(u, v, d+w)
    dfs(0, -1, 0)
    print(*ans, sep="\n")

=======
Suggestion 5

def main():
    N = int(input())
    tree = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        tree[u-1].append((v-1, w))
        tree[v-1].append((u-1, w))
    color = [-1] * N
    color[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for u, w in tree[v]:
            if color[u] != -1:
                continue
            color[u] = color[v] ^ (w % 2)
            stack.append(u)
    print(*color, sep='\n')

=======
Suggestion 6

def main():
    n = int(input())
    edges = []
    for i in range(n-1):
        edges.append(list(map(int, input().split())))

    colors = [-1 for _ in range(n)]
    colors[0] = 0
    q = [0]
    while len(q) > 0:
        v = q.pop()
        for edge in edges:
            if edge[0] == v and colors[edge[1]-1] == -1:
                colors[edge[1]-1] = (colors[v]+edge[2])%2
                q.append(edge[1]-1)
            elif edge[1] == v and colors[edge[0]-1] == -1:
                colors[edge[0]-1] = (colors[v]+edge[2])%2
                q.append(edge[0]-1)
    for color in colors:
        print(color)

=======
Suggestion 7

def dfs(u, c):
    color[u] = c
    for v, w in adj[u]:
        if color[v] == -1:
            dfs(v, c ^ w)

n = int(input())
adj = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append((v, w % 2))
    adj[v].append((u, w % 2))

color = [-1] * n
dfs(0, 0)
for c in color:
    print(c)

=======
Suggestion 8

def dfs(v, c):
    color[v] = c
    for i in range(len(edge[v])):
        if color[edge[v][i]] == -1:
            dfs(edge[v][i], c ^ 1)

n = int(input())
edge = [[] for i in range(n)]
color = [-1 for i in range(n)]
for i in range(n - 1):
    a, b, w = map(int, input().split())
    edge[a - 1].append(b - 1)
    edge[b - 1].append(a - 1)
dfs(0, 0)
for i in range(n):
    print(color[i])

=======
Suggestion 9

def main():
    n = int(input())
    u = []
    v = []
    w = []
    for i in range(n-1):
        u_i, v_i, w_i = map(int, input().split())
        u.append(u_i)
        v.append(v_i)
        w.append(w_i)
    ans = [0] * n
    for i in range(n-1):
        if w[i] % 2 == 0:
            ans[v[i]-1] = ans[u[i]-1]
        else:
            ans[v[i]-1] = 1 - ans[u[i]-1]
    for i in range(n):
        print(ans[i])

=======
Suggestion 10

def main():
    n = int(input())
    edges = []
    for i in range(n-1):
        u, v, w = map(int, input().split())
        edges.append((u-1, v-1, w))
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    color = [-1]*n
    color[0] = 0
    stack = [0]
    while stack:
        u = stack.pop()
        for v, w in adj[u]:
            if color[v] != -1:
                continue
            color[v] = 1-color[u] if w%2 else color[u]
            stack.append(v)
    print(*color, sep='\n')
