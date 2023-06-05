Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N,X,Y = map(int,input().split())
    U = []
    V = []
    for i in range(N-1):
        u,v = map(int,input().split())
        U.append(u)
        V.append(v)
    #print(U)
    #print(V)
    #print(N,X,Y)
    #print(N)
    #print(U)
    #prin

=======
Suggestion 2

def build_tree(edges):
    tree = {}
    for edge in edges:
        if edge[0] not in tree.keys():
            tree[edge[0]] = []
        if edge[1] not in tree.keys():
            tree[edge[1]] = []
        tree[edge[0]].append(edge[1])
        tree[edge[1]].append(edge[0])
    return tree

=======
Suggestion 3

def dfs(i):
    global ans
    global visited
    global G
    visited[i] = True
    ans.append(i)
    for j in G[i]:
        if visited[j] == False:
            dfs(j)
            ans.append(i)

N,X,Y = map(int,input().split())
U = [0] * (N-1)
V = [0] * (N-1)
G = [[] for _ in range(N+1)]
for i in range(N-1):
    U[i],V[i] = map(int,input().split())
    G[U[i]].append(V[i])
    G[V[i]].append(U[i])

visited = [False] * (N+1)
ans = []
dfs(X)
ans.append(X)
ans = ans[::-1]
ans = ans[ans.index(Y):]
for i in ans:
    print(i,end=' ')
print()

=======
Suggestion 4

def dfs(v, p):
    global ans
    ans.append(v+1)
    for nv in to[v]:
        if nv == p:
            continue
        dfs(nv, v)
        ans.append(v+1)

n, x, y = map(int, input().split())
x -= 1
y -= 1
to = [[] for _ in range(n)]
for _ in range(n-1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    to[u].append(v)
    to[v].append(u)
ans = []
dfs(x, -1)
print(*ans)

=======
Suggestion 5

def find_path(u,v):
    path = []
    while u != v:
        path.append(u)
        u = parent[u]
    path.append(v)
    return path

=======
Suggestion 6

def input():
    N, X, Y = map(int, input().split())
    tree = [[] for i in range(N)]
    for i in range(N-1):
        U, V = map(int, input().split())
        tree[U-1].append(V-1)
        tree[V-1].append(U-1)
    return N, X-1, Y-1, tree

=======
Suggestion 7

def get_path():
    n, x, y = map(int, input().split())
    x -= 1
    y -= 1
    tree = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        tree[u].append(v)
        tree[v].append(u)
    dist = [-1] * n
    dist[x] = 0
    que = [x]
    while que:
        v = que.pop()
        for nv in tree[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            que.append(nv)
    path = [y]
    v = y
    while v != x:
        for nv in tree[v]:
            if dist[nv] == dist[v] - 1:
                v = nv
                path.append(v)
                break
    path.reverse()
    return path

=======
Suggestion 8

def main():
    N, X, Y = map(int, input().split())
    #print(N, X, Y)
    tree = {}
    for i in range(N-1):
        U, V = map(int, input().split())
        #print(U, V)
        if U not in tree:
            tree[U] = [V]
        else:
            tree[U].append(V)
        if V not in tree:
            tree[V] = [U]
        else:
            tree[V].append(U)
    #print(tree)
    path = [X]
    while path[-1] != Y:
        if len(tree[path[-1]]) == 1:
            path.pop()
        else:
            for i in range(len(tree[path[-1]])-1, -1, -1):
                if tree[path[-1]][i] == path[-2]:
                    tree[path[-1]].pop(i)
            path.append(tree[path[-1]][-1])
    print(*path)

=======
Suggestion 9

def main():
    n,x,y = map(int,input().split())
    u = [0] * (n-1)
    v = [0] * (n-1)
    for i in range(n-1):
        u[i],v[i] = map(int,input().split())

    for i in range(n-1):
        if u[i] == x and v[i] == y:
            print(x,y)
            break
        elif u[i] == y and v[i] == x:
            print(y,x)
            break
        elif u[i] == x:
            print(u[i],end=" ")
            x = v[i]
        elif v[i] == x:
            print(v[i],end=" ")
            x = u[i]
        elif u[i] == y:
            print(u[i],end=" ")
            y = v[i]
        elif v[i] == y:
            print(v[i],end=" ")
            y = u[i]

=======
Suggestion 10

def main():
    n,x,y = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    parent = [0]*(n+1)
    parent[x] = -1
    stack = [x]
    while stack:
        node = stack.pop()
        for child in graph[node]:
            if parent[child] == 0:
                parent[child] = node
                stack.append(child)
    path = []
    node = y
    while node != -1:
        path.append(node)
        node = parent[node]
    print(*path[::-1])
