Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def f(x):
    if x == 0:
        return 1
    else:
        return 0

N = int(input())
a = []
b = []
for i in range(N-1):
    a.append(int(input().split()[0]))
    b.append(int(input().split()[1]))

color = [0] * (N + 1)
color[1] = 1
for i in range(N - 1):
    if color[a[i]] == color[b[i]]:
        color[b[i]] = f(color[b[i]])
    color[b[i]] = color[b[i]]
    color[b[i]+1] = color[b[i]] + 1
    #print(color)
print(max(color))
for i in range(N-1):
    print(color[b[i]])

=======
Suggestion 3

def dfs(v, p, c):
    color[c] = True
    ans[v] = c
    k = 1
    for w in g[v]:
        if w == p:
            continue
        while color[k]:
            k += 1
        dfs(w, v, k)

n = int(input())
g = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

ans = [0] * n
color = [False] * (n+1)
dfs(0, -1, 1)
print(max(ans))
for i in range(n-1):
    print(ans[i+1])

=======
Suggestion 4

def dfs(v, p, c):
    global color, G
    color[v] = c
    for i in range(len(G[v])):
        if G[v][i] == p:
            continue
        dfs(G[v][i], v, (c+1)%len(G[v]))

n = int(input())
G = [[] for i in range(n)]
color = [0]*n
for i in range(n-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
dfs(0, -1, 0)
print(max(color)+1)
for i in range(n-1):
    print(color[i]+1)

=======
Suggestion 5

def dfs(G, v, c):
    color[v] = c
    for i in G[v]:
        if color[i] == 0:
            dfs(G, i, c)

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

color = [0]*N
color[0] = 1
for i in G[0]:
    color[i] = 2
for i in G[0]:
    dfs(G, i, color[i])
print(max(color))
for i in range(N-1):
    print(color[i+1])

=======
Suggestion 6

def dfs(node, parent, color):
    c = 1
    for child in node:
        if child == parent:
            continue
        if c == color:
            c += 1
        ans[child] = c
        dfs(tree[child], node, c)
        c += 1

N = int(input())
tree = [[] for _ in range(N+1)]
ans = [0] * (N+1)
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

dfs(tree[1], 0, 0)
print(max(ans))
for i in range(2, N+1):
    print(ans[i])

=======
Suggestion 7

def main():
    N = int(input())
    edges = []
    for i in range(N-1):
        a,b = map(int,input().split())
        edges.append((a,b))
    print(edges)
    #edges = [(1,2),(2,3)]
    #edges = [(1,2),(2,3),(2,4),(2,5),(4,7),(5,6),(6,8)]
    #edges = [(1,2),(1,3),(1,4),(1,5),(1,6)]
    #edges = [(1,2),(2,3),(2,4),(2,5),(4,7),(5,6),(6,8)]
    #edges = [(1,2),(1,3),(1,4),(1,5),(1,6)]
    #edges = [(1,2),(2,3),(2,4),(2,5),(4,7),(5,6),(6,8)]
    #edges = [(1,2),(1,3),(1,4),(1,5),(1,6)]
    #edges = [(1,2),(2,3),(2,4),(2,5),(4,7),(5,6),(6,8)]
    #edges = [(1,2),(1,3),(1,4),(1,5),(1,6)]
    #edges = [(1,2),(2,3),(2,4),(2,5),(4,7),(5,6),(6,8)]
    #edges = [(1,2),(1,3),(1,4),(1,5),(1,6)]
    #edges = [(1,2),(2,3),(2,4),(2,5),(4,7),(5,6),(6,8)]
    #edges = [(1,2),(1,3),(1,4),(1,5),(1,6)]
    #edges = [(1,2),(2,3),(2,4),(2,5),(4,7),(5,6),(6,8)]
    #edges = [(1,2),(1,3),(1,4),(1,5),(1,6)]
    #edges = [(1,2),(2,3),(2,4),(2,5),(4,7),(5,6),(6,8)]
    #edges = [(1

=======
Suggestion 8

def dfs(v,p,c):
    color[c] = True
    for i in g[v]:
        if i == p:
            continue
        for j in range(1,k+1):
            if not color[j]:
                ans[i] = j
                dfs(i,v,j)
                break

n = int(input())
g = [[] for _ in range(n+1)]
ans = [0] * (n+1)
color = [False] * (n+1)
for _ in range(n-1):
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)
k = 0
for i in range(1,n+1):
    k = max(k,len(g[i]))
print(k)
ans[1] = 1
dfs(1,-1,1)
for i in range(1,n+1):
    print(ans[i])

=======
Suggestion 9

def dfs(v, p, c):
    global color
    color[c].append(v)
    for u in tree[v]:
        if u == p:
            continue
        dfs(u, v, c+1)

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

color = [[] for _ in range(n+1)]
dfs(1, -1, 1)
max_color = max(len(color[i]) for i in range(1, n+1))
print(max_color)
for i in range(1, n+1):
    print(i)
    if len(color[i]) == 0:
        continue
    print(' '.join(map(str, color[i])))
