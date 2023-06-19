Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    pass

=======
Suggestion 2

def main():
    pass

=======
Suggestion 3

def dfs(v,p,c):
    color[v] = c
    for i in range(len(G[v])):
        if G[v][i] == p:continue
        if color[G[v][i]] != -1:continue
        dfs(G[v][i],v,c^D[v][i])

N = int(input())
G = [[] for i in range(N)]
D = [[] for i in range(N)]
for i in range(N-1):
    u,v,w = map(int,input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)
    D[u].append(w%2)
    D[v].append(w%2)

color = [-1]*N
dfs(0,-1,0)
for i in range(N):
    print(color[i])

=======
Suggestion 4

def dfs(s, color):
    global ans
    ans[s] = color
    for t, w in G[s]:
        if ans[t] != -1:
            continue
        if w % 2 == 0:
            dfs(t, color)
        else:
            dfs(t, 1 - color)
    return

N = int(input())
G = [[] for i in range(N)]
ans = [-1 for i in range(N)]
for i in range(N - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append((v, w))
    G[v].append((u, w))
dfs(0, 0)
for i in range(N):
    print(ans[i])

=======
Suggestion 5

def dfs(v, c):
    color[v] = c
    for i in range(len(G[v])):
        if color[G[v][i]] == -1:
            dfs(G[v][i], 1 - c)

N = int(input())
G = [[] for i in range(N)]
color = [-1 for i in range(N)]
for i in range(N - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    if w % 2 == 0:
        G[u].append(v)
        G[v].append(u)
dfs(0, 0)
for i in range(N):
    print(color[i])

=======
Suggestion 6

def main():
    N = int(input())
    edges = []
    for i in range(N-1):
        edge = list(map(int, input().split()))
        edges.append(edge)
    #print(edges)
    #edges = [[1, 2, 2], [2, 3, 1]]
    #edges = [[2, 5, 2], [2, 3, 10], [1, 3, 8], [3, 4, 2]]
    #print(edges)
    #edges.sort(key=lambda x:x[2])
    #print(edges)
    #print(edges)
    #print(edges[0][0])
    #print(edges[0][1])
    #print(edges[0][2])
    #print(edges[1][0])
    #print(edges[1][1])
    #print(edges[1][2])
    #print(edges[2][0])
    #print(edges[2][1])
    #print(edges[2][2])
    #print(edges[3][0])
    #print(edges[3][1])
    #print(edges[3][2])
    #print(edges[4][0])
    #print(edges[4][1])
    #print(edges[4][2])
    #print(edges[5][0])
    #print(edges[5][1])
    #print(edges[5][2])
    #print(edges[6][0])
    #print(edges[6][1])
    #print(edges[6][2])
    #print(edges[7][0])
    #print(edges[7][1])
    #print(edges[7][2])
    #print(edges[8][0])
    #print(edges[8][1])
    #print(edges[8][2])
    #print(edges[9][0])
    #print(edges[9][1])
    #print(edges[9][2])
    #print(edges[10][0])
    #print(edges[10][1])
    #print(edges[10][2])
    #print(edges[11][0])
    #print(edges[11][1])
    #print(edges[11][2])
    #print(edges[12][0])
    #print(edges[12][1])
    #print(edges[12][2])
    #print(edges[13][0])
    #print(edges[13][1])

=======
Suggestion 7

def dfs(u,color):
    global G
    global visited
    global ans
    global color
    visited[u] = True
    color[u] = c
    for v in G[u]:
        if visited[v]:
            continue
        dfs(v,1-c)

N = int(input())
G = [[] for i in range(N)]
for i in range(N-1):
    u,v,w = map(int,input().split())
    G[u-1].append(v-1)
    G[v-1].append(u-1)
visited = [False]*N
color = [0]*N
ans = []
dfs(0,0)

for i in range(N):
    print(color[i])

=======
Suggestion 8

def dfs(u, c, d):
    color[u] = c
    for v, w in adj[u]:
        if color[v] != -1:
            continue
        dfs(v, c ^ (w & 1), d + w)

n = int(input())
adj = [[] for _ in range(n)]
color = [-1] * n

for _ in range(n - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append((v, w))
    adj[v].append((u, w))

dfs(0, 0, 0)

for i in range(n):
    print(color[i])
