Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def dfs(start, parent, color):
    c = 1
    for to in edges[start]:
        if to == parent:
            continue
        if c == color:
            c += 1
        ans.append((start, to, c))
        dfs(to, start, c)
        c += 1


n = int(input())
edges = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

ans = []
dfs(1, 0, 0)
print(len(ans))
for a, b, c in ans:
    print(c)

=======
Suggestion 2

def dfs(v,p=-1):
    global k
    c = 1
    for u in g[v]:
        if u==p:continue
        if c==c1 or c==p1:c+=1
        ans[u] = c
        c1,p1 = c,p
        c+=1
        k = max(k,c)
        dfs(u,v)

n = int(input())
g = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)
ans = [0]*(n+1)
k = 0
dfs(1)
print(k)
for i in range(1,n):
    print(ans[i])

=======
Suggestion 3

def dfs(v, p, c):
    color[c] = True
    ans[v] = c
    k = 1
    for i in range(len(g[v])):
        if g[v][i] == p: continue
        while color[k]: k += 1
        dfs(g[v][i], v, k)

n = int(input())
g = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

ans = [0] * (n+1)
color = [False] * (n+1)
dfs(1, 0, 0)
print(max(ans))
for i in range(1, n):
    print(ans[i])

=======
Suggestion 4

def dfs(v,p):
    c = 1
    for i in g[v]:
        if i == p:
            continue
        if c == color[p]:
            c += 1
        color[i] = c
        dfs(i,v)
        c += 1

n = int(input())
g = [[] for i in range(n+1)]
for i in range(n-1):
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)

color = [0] * (n+1)
dfs(1,0)
print(max(color))
for i in range(1,n):
    print(color[i])

=======
Suggestion 5

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
ans = [0] * N
for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

dfs(0, -1, -1)
print(max(ans))
for i in ans:
    print(i)

=======
Suggestion 6

def main():
    pass

=======
Suggestion 7

def get_input():
    n = int(input())
    edges = []
    for i in range(n-1):
        edge = list(map(int,input().split()))
        edges.append(edge)
    return n, edges

=======
Suggestion 8

def main():
    N = int(input())
    a = []
    b = []
    for i in range(N-1):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    print(a)
    print(b)

=======
Suggestion 9

def dfs(v, p, c):
    color = 1
    for u in g[v]:
        if u == p:
            continue
        if color == c:
            color += 1
        ans[(v, u)] = ans[(u, v)] = color
        dfs(u, v, color)
        color += 1

n = int(input())
g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

ans = {}
dfs(0, -1, -1)
print(max(ans.values()))
for i in range(n - 1):
    print(ans[(i, i + 1)])
