Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def addEdge(u, v, w):
    global edges
    global edgeNum
    global nodes
    global nodeNum

    edges[edgeNum] = (u, v, w)
    nodes[u].append(edgeNum)
    nodes[v].append(edgeNum)
    edgeNum += 1

=======
Suggestion 2

def main():
    pass

=======
Suggestion 3

def dfs(v, color, c):
    color[v] = c
    for i in range(len(g[v])):
        if color[g[v][i]] == -1:
            dfs(g[v][i], color, c ^ w[v][i])

n = int(input())
g = [[] for i in range(n)]
w = [[] for i in range(n)]
for i in range(n - 1):
    u, v, ww = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)
    w[u].append(ww % 2)
    w[v].append(ww % 2)

color = [-1] * n
dfs(0, color, 0)
for i in range(n):
    print(color[i])

=======
Suggestion 4

def dfs(s, v, c):
    color[v] = c
    for i in range(len(graph[v])):
        if color[graph[v][i]] == -1:
            if not dfs(s, graph[v][i], c ^ 1):
                return False
        elif color[graph[v][i]] == c:
            return False
    return True

=======
Suggestion 5

def dfs(v,p,c):
    color[v] = c
    for e in G[v]:
        if e[0] == p:
            continue
        if e[1] % 2 == 0:
            dfs(e[0],v,c)
        else:
            dfs(e[0],v,1-c)

N = int(input())
G = [[] for i in range(N)]
for i in range(N-1):
    u,v,w = map(int,input().split())
    u -= 1
    v -= 1
    G[u].append((v,w))
    G[v].append((u,w))
color = [0]*N
dfs(0,-1,0)
print("\n".join(map(str,color)))

=======
Suggestion 6

def dfs(cur, col):
    color[cur] = col
    for i in range(len(graph[cur])):
        if color[graph[cur][i]] == -1:
            dfs(graph[cur][i], col ^ cost[cur][i])

N = int(input())
graph = [[] for i in range(N)]
cost = [[] for i in range(N)]
color = [-1 for i in range(N)]

for i in range(N - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)
    cost[u].append(w % 2)
    cost[v].append(w % 2)

dfs(0, 0)
for i in range(N):
    print(color[i])

=======
Suggestion 7

def dfs(node, color, visited, tree, ans):
    visited[node] = True
    ans[node] = color
    for i in tree[node]:
        if visited[i] == False:
            if color == 0:
                dfs(i, 1, visited, tree, ans)
            else:
                dfs(i, 0, visited, tree, ans)

n = int(input())
tree = [[] for i in range(n)]
for i in range(n - 1):
    u, v, w = map(int, input().split())
    tree[u - 1].append(v - 1)
    tree[v - 1].append(u - 1)

visited = [False] * n
ans = [0] * n
dfs(0, 0, visited, tree, ans)

for i in ans:
    print(i)
