Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,x,y = map(int,input().split())
    x -= 1
    y -= 1
    graph = [[] for _ in range(n)]
    for i in range(n-1):
        u,v = map(int,input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    #print(graph)

=======
Suggestion 2

def dfs(v, p, g, path):
    path.append(v)
    for nv in g[v]:
        if nv != p:
            dfs(nv, v, g, path)
            path.append(v)

=======
Suggestion 3

def main():
  n,x,y = map(int,input().split())
  edge = [[] for _ in range(n+1)]
  for _ in range(n-1):
    u,v = map(int,input().split())
    edge[u].append(v)
    edge[v].append(u)
  #print(edge)
  #xからyへのパスを探す
  #dfsで探索
  #print(edge[x])
  #print(edge[y])
  #print(edge[x][0])
  #print(edge[y][0])
  #print(edge[edge[x][0]])
  #print(edge[edge[y][0]])
  #print(edge[edge[y][0]][0])
  #print(edge[edge[y][0]][1])
  #print(edge[edge[y][0]][2])
  #print(edge[edge[y][0]][3])
  #print(edge[edge[y][0]][4])
  #print(edge[edge[y][0]][5])
  #print(edge[edge[y][0]][6])
  #print(edge[edge[y][0]][7])
  #print(edge[edge[y][0]][8])
  #print(edge[edge[y][0]][9])
  #print(edge[edge[y][0]][10])
  #print(edge[edge[y][0]][11])
  #print(edge[edge[y][0]][12])
  #print(edge[edge[y][0]][13])
  #print(edge[edge[y][0]][14])
  #print(edge[edge[y][0]][15])
  #print(edge[edge[y][0]][16])
  #print(edge[edge[y][0]][17])
  #print(edge[edge[y][0]][18])
  #print(edge[edge[y][0]][19])
  #print(edge[edge[y][0]][20])
  #print(edge[edge[y][0]][21])
  #print(edge[edge[y][0]][22])
  #print(edge[edge[y][0]][23])
  #print(edge[edge[y][0]][24])
  #print(edge[edge[y][0]][25])
  #print(edge[edge[y][0]][26])
  #print(edge[edge[y][0]][27])
  #print(edge[edge[y][0]][28])
  #print(edge[edge[y][0]][29])
  #print(edge[edge[y][0]][30])
  #print(edge[edge[y][0]][31])
  #print(edge[edge[y][0]][32])
  #print(edge[edge

=======
Suggestion 4

def dfs(v,parent):
    for u in g[v]:
        if u==parent:
            continue
        else:
            depth[u]=depth[v]+1
            dfs(u,v)

n,x,y=map(int,input().split())
x-=1
y-=1
g=[[] for _ in range(n)]
for _ in range(n-1):
    a,b=map(int,input().split())
    a-=1
    b-=1
    g[a].append(b)
    g[b].append(a)

depth=[0]*n
dfs(x,-1)

ans=[0]*n
for i in range(n):
    ans[depth[i]]+=1
print(ans[depth[y]]-1)

=======
Suggestion 5

def dfs(v, p):
    for u in g[v]:
        if u == p:
            continue
        dfs(u, v)
        ans.append(u)
    ans.append(p)
    return

n, x, y = map(int, input().split())
g = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
ans = []
dfs(x, y)
dfs(y, x)
ans.reverse()
print(*ans)

=======
Suggestion 6

def dfs(v, p):
    global ans
    ans.append(v)
    for i in g[v]:
        if i == p:
            continue
        dfs(i, v)
        ans.append(v)
    return

n, x, y = map(int, input().split())
g = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
ans = []
dfs(x, -1)
ans.append(x)
dfs(y, -1)
ans.append(y)
print(*ans)

=======
Suggestion 7

def dfs(v, p, g, d, ans):
    ans.append(v)
    for u in g[v]:
        if u == p:
            continue
        if d[u] == -1:
            d[u] = d[v] + 1
            dfs(u, v, g, d, ans)
            ans.append(v)
            d[v] = d[u] + 1
            return
    ans.pop()

n, x, y = map(int, input().split())
x -= 1
y -= 1
g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

d = [-1] * n
d[x] = 0
ans = []
dfs(y, -1, g, d, ans)
print(*[v + 1 for v in ans])

=======
Suggestion 8

def dfs(v, p):
    for u in g[v]:
        if u == p:
            continue
        depth[u] = depth[v] + 1
        dfs(u, v)

n, x, y = map(int, input().split())
x -= 1
y -= 1

g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

depth = [0] * n
dfs(x, -1)
print(depth[y])

=======
Suggestion 9

def main():
    n,x,y = map(int,input().split())
    s = [0] * (n+1)
    for i in range(n-1):
        u,v = map(int,input().split())
        s[u] += 1
        s[v] += 1
    if s[x] < s[y]:
        x,y = y,x
    print(x,y)
    return

=======
Suggestion 10

def dfs(v, p):
    for u in G[v]:
        if u == p:
            continue
        dist[u] = dist[v] + 1
        dfs(u, v)

N, X, Y = map(int, input().split())
X -= 1
Y -= 1
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
dist = [0] * N
dfs(X, -1)
print(*sorted(dist[Y:]))
