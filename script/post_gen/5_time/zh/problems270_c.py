Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,x,y = map(int,input().split())
    x-=1
    y-=1
    edge = [[] for _ in range(n)]
    for _ in range(n-1):
        u,v = map(int,input().split())
        u-=1
        v-=1
        edge[u].append(v)
        edge[v].append(u)
    parent = [0]*n
    parent[x] = x
    stack = [x]
    while stack:
        v = stack.pop()
        for u in edge[v]:
            if u == parent[v]:
                continue
            parent[u] = v
            stack.append(u)
    ans = []
    while y != x:
        ans.append(y)
        y = parent[y]
    ans.append(x)
    print(*[v+1 for v in reversed(ans)])

=======
Suggestion 2

def main():
    N,X,Y = map(int,input().split())
    U = []
    V = []
    for i in range(N-1):
        u,v = map(int,input().split())
        U.append(u)
        V.append(v)
    print(U)
    print(V)

=======
Suggestion 3

def main():
    N,X,Y = map(int,input().split())
    U = [0]*(N-1)
    V = [0]*(N-1)
    for i in range(N-1):
        U[i],V[i] = map(int,input().split())
    ans = []
    for i in range(N-1):
        if U[i] == X and V[i] == Y:
            ans.append(i)
        elif U[i] == Y and V[i] == X:
            ans.append(i)
    if len(ans) == 0:
        print(-1)
    else:
        print(ans[0])

=======
Suggestion 4

def get_input():
    N, X, Y = map(int, input().split())
    tree = []
    for i in range(N - 1):
        tree.append(list(map(int, input().split())))
    return N, X, Y, tree

=======
Suggestion 5

def dfs(now,pre):
    global ans
    ans.append(now)
    for i in range(len(edge[now])):
        if edge[now][i] != pre:
            dfs(edge[now][i],now)
            ans.append(now)
    return

N,X,Y = map(int,input().split())
edge = [[] for i in range(N+1)]
for i in range(N-1):
    u,v = map(int,input().split())
    edge[u].append(v)
    edge[v].append(u)
ans = []
dfs(X,-1)
ans.append(X)
ans.reverse()
dfs(Y,-1)
ans.append(Y)
ans = list(set(ans))
ans.sort()
print(*ans)

=======
Suggestion 6

def dfs(x, y):
    if x == y:
        return [x]
    for i in range(len(G[x])):
        if not visited[G[x][i]]:
            visited[G[x][i]] = True
            res = dfs(G[x][i], y)
            if res:
                res.insert(0, x)
                return res
    return []

N, X, Y = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

visited = [False] * N
visited[X-1] = True
res = dfs(X-1, Y-1)
print(*[i+1 for i in res])

=======
Suggestion 7

def main():
    n, x, y = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(n-1)]
    edges.sort()
    print(edges)
    #print(edges)
    #for i in range(n-1):
    #    if edges[i][0] == x and edges[i][1] == y:
    #        print(edges[i][0], edges[i][1])
    #    elif edges[i][0] == x:
    #        print(edges[i][0], edges[i][1])
    #    elif edges[i][1] == y:
    #        print(edges[i][0], edges[i][1])
    #    elif edges[i][0] == y:
    #        print(edges[i][0], edges[i][1])
    #    elif edges[i][1] == x:
    #        print(edges[i][0], edges[i][1])
    #    else:
    #        continue
    #print(edges)
    #for i in range(n-1):
    #    if edges[i][0] == x:
    #        print(edges[i][0], edges[i][1])
    #    elif edges[i][1] == y:
    #        print(edges[i][0], edges[i][1])
    #    elif edges[i][1] == x:
    #        print(edges[i][0], edges[i][1])
    #    elif edges[i][0] == y:
    #        print(edges[i][0], edges[i][1])
    #    else:
    #        continue
    #print(edges)
    #for i in range(n-1):
    #    if edges[i][0] == x:
    #        print(edges[i][0], edges[i][1])
    #    elif edges[i][0] == y:
    #        print(edges[i][0], edges[i][1])
    #    elif edges[i][1] == x:
    #        print(edges[i][0], edges[i][1])
    #    elif edges[i][1] == y:
    #        print(edges[i][0], edges[i][1])
    #    else:
    #        continue
    #print(edges)
    #for i in range(n-1):
    #    if edges[i][1] == x:
    #        print(edges[i][0

=======
Suggestion 8

def main():
    N,X,Y = map(int,input().split())
    edges = []
    for i in range(N-1):
        edges.append(list(map(int,input().split())))
    #print(edges)
    #print(N,X,Y)
    #print(edges)
    graph = [[0 for i in range(N)] for j in range(N)]
    #print(graph)
    for edge in edges:
        graph[edge[0]-1][edge[1]-1] = 1
        graph[edge[1]-1][edge[0]-1] = 1
    #print(graph)
    #print(graph)
    #print(graph[1])
    #print(graph[2])
    #print(graph[3])
    #print(graph[4])
    #print(graph[5])
    #print(graph[6])
    #print(graph[7])
    #print(graph[8])
    #print(graph[9])
    #print(graph[10])
    #print(graph[11])
    #print(graph[12])
    #print(graph[13])
    #print(graph[14])
    #print(graph[15])
    #print(graph[16])
    #print(graph[17])
    #print(graph[18])
    #print(graph[19])
    #print(graph[20])
    #print(graph[21])
    #print(graph[22])
    #print(graph[23])
    #print(graph[24])
    #print(graph[25])
    #print(graph[26])
    #print(graph[27])
    #print(graph[28])
    #print(graph[29])
    #print(graph[30])
    #print(graph[31])
    #print(graph[32])
    #print(graph[33])
    #print(graph[34])
    #print(graph[35])
    #print(graph[36])
    #print(graph[37])
    #print(graph[38])
    #print(graph[39])
    #print(graph[40])
    #print(graph[41])
    #print(graph[42])
    #print(graph[43])
    #print(graph[44])
    #print(graph[45])
    #print(graph[46])
    #print(graph[47])
    #print(graph[48])
    #print(graph[49])
    #print(graph[50])
    #print(graph[51])
    #print(graph[52])
    #print(graph[53])
    #

=======
Suggestion 9

def main():
    N,X,Y = map(int,input().split())
    U = [0] * (N-1)
    V = [0] * (N-1)
    for i in range(N-1):
        U[i],V[i] = map(int,input().split())

    print(U)
    print(V)
    print(N,X,Y)

=======
Suggestion 10

def main():
    pass
