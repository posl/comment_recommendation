Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    tree = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        tree[a - 1].append(b - 1)
        tree[b - 1].append(a - 1)

    used = [False] * n
    ans = [0] * (n - 1)

    def dfs(v, p):
        c = 1
        for u in tree[v]:
            if u == p:
                continue
            if c == ans[v]:
                c += 1
            ans[u] = c
            c += 1
            dfs(u, v)

    dfs(0, -1)
    print(max(ans))
    for c in ans:
        print(c)

=======
Suggestion 2

def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n-1)]
    graph = [[] for _ in range(n)]
    for a, b in ab:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    color = [0] * n
    color[0] = 1
    color[1] = 2
    color[2] = 3
    queue = [0]
    while queue:
        v = queue.pop()
        c = color[v]
        for u in graph[v]:
            if color[u] == 0:
                c += 1
                if c > 3:
                    c = 1
                color[u] = c
                queue.append(u)
    print(max(color))
    for i in range(n-1):
        print(color[ab[i][0]-1])

=======
Suggestion 3

def dfs(v, p):
    global c
    color = 1
    for u in G[v]:
        if u == p:
            continue
        if color == c[v]:
            color += 1
        c[u] = color
        color += 1
        dfs(u, v)

N = int(input())
G = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

c = [0] * (N+1)
c[1] = 1
dfs(1, -1)
print(max(c))
for i in range(1, N):
    print(c[i+1])

=======
Suggestion 4

def dfs(v, p, c):
    color = 1
    for i in G[v]:
        if i == p:
            continue
        if color == c:
            color += 1
        ans[i] = color
        dfs(i, v, color)
        color += 1

N = int(input())
G = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

ans = [0] * N
dfs(0, -1, -1)
print(max(ans))
for i in ans:
    print(i)

=======
Suggestion 5

def dfs(v, p=-1):
    global k
    global ans
    c = 1
    for u in G[v]:
        if u == p:
            continue
        if c == ans[v]:
            c += 1
        ans[u] = c
        c += 1
        k = max(k, c - 1)
        dfs(u, v)

n = int(input())
G = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
ans = [0] * n
k = 0
dfs(0)
print(k)
for i in range(n - 1):
    print(ans[i])

=======
Suggestion 6

def dfs(u, p, c):
    global ans
    ans = max(ans, c)
    k = 1
    for v in G[u]:
        if v == p:
            continue
        if k == c:
            k += 1
        print(k)
        dfs(v, u, k)
        k += 1

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    G[a].append(b)
    G[b].append(a)
ans = 0
dfs(0, -1, 0)
print(ans)

=======
Suggestion 7

def dfs(v, p, c):
    color = 1
    for u in tree[v]:
        if u == p:
            continue
        if color == c:
            color += 1
        ans[u] = color
        dfs(u, v, color)
        color += 1

n = int(input())
tree = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)

ans = [0] * n
ans[0] = 1
dfs(0, -1, 1)
print(max(ans))
for i in range(n-1):
    print(ans[i+1])

=======
Suggestion 8

def main():
    N = int(input())
    edges = []
    for i in range(N-1):
        a, b = map(int, input().split())
        edges.append([a, b, i])

    adj = [[] for _ in range(N+1)]
    for a, b, i in edges:
        adj[a].append((b, i))
        adj[b].append((a, i))

    ans = [0] * (N-1)
    used = [False] * (N+1)
    used[1] = True
    color = 0
    for a, b, i in edges:
        if ans[i] != 0:
            continue
        color += 1
        ans[i] = color
        used_color = [False] * (N+1)
        used_color[ans[i]] = True
        stack = [(a, b), (b, a)]
        while stack:
            v, p = stack.pop()
            for nv, ni in adj[v]:
                if nv == p:
                    continue
                if ans[ni] != 0:
                    continue
                while used_color[color]:
                    color += 1
                ans[ni] = color
                used_color[color] = True
                stack.append((nv, v))

    print(max(ans))
    for a in ans:
        print(a)

=======
Suggestion 9

def main():
    N = int(input())
    ab = [list(map(int, input().split())) for _ in range(N-1)]
    #print(N)
    #print(ab)
    #print(len(ab))
    #print(ab[0])
    #print(ab[0][0])
    #print(ab[0][1])
    
    #print(ab[0][0])
    #print(ab[0][1])
    #print(ab[1][0])
    #print(ab[1][1])
    
    #print(ab[0][0])
    #print(ab[0][1])
    #print(ab[1][0])
    #print(ab[1][1])
    
    #print(ab[0][0])
    #print(ab[0][1])
    #print(ab[1][0])
    #print(ab[1][1])
    
    #print(ab[0][0])
    #print(ab[0][1])
    #print(ab[1][0])
    #print(ab[1][1])
    
    #print(ab[0][0])
    #print(ab[0][1])
    #print(ab[1][0])
    #print(ab[1][1])
    
    #print(ab[0][0])
    #print(ab[0][1])
    #print(ab[1][0])
    #print(ab[1][1])
    
    #print(ab[0][0])
    #print(ab[0][1])
    #print(ab[1][0])
    #print(ab[1][1])
    
    #print(ab[0][0])
    #print(ab[0][1])
    #print(ab[1][0])
    #print(ab[1][1])
    colors = []
    for i in range(N-1):
        colors.append(0)
    #print(colors)
    
    #print(len(colors))
    #print(colors[0])
    #print(colors[1])
    #print(colors[2])
    #print(colors[3])
    #print(colors[4])
    #print(colors[5])
    #print(colors[6])
    #print(colors[7])
    
    #print(len(colors))
    #print(colors[0])
    #print(colors[1])
    #print(colors[2])
    #print(colors[3])
    #print(colors[4])
    #print(colors[5

=======
Suggestion 10

def dfs(v, p, c):
    global color
    color[c] += 1
    for u in g[v]:
        if u == p:
            continue
        dfs(u, v, c)
    return

N = int(input())
g = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

color = [0] * N
dfs(0, -1, 0)
print(max(color))
for i in range(N-1):
    print(color[i+1] if color[i+1] > 0 else 1)
