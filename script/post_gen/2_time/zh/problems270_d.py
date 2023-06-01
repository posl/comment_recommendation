Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X, Y = map(int, input().split())
    edges = []
    for i in range(N-1):
        U_i, V_i = map(int, input().split())
        edges.append([U_i, V_i])

    print(edges)

=======
Suggestion 2

def main():
    N,X,Y = map(int,input().split())
    edge = []
    for i in range(N-1):
        edge.append(list(map(int,input().split())))
    print(edge)

=======
Suggestion 3

def main():
    N, X, Y = map(int, input().split())
    X, Y = X-1, Y-1
    tree = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        tree[u-1].append(v-1)
        tree[v-1].append(u-1)
    # print(tree)
    # print(X, Y)
    # X, Y = 1, 2
    # tree = [[1, 2], [0, 3, 4], [0, 5, 6], [1], [1], [2], [2]]
    # print(tree)
    # print(X, Y)
    # X, Y = 0, 6
    # tree = [[1], [0, 2, 3], [1, 4, 5], [1], [2], [2], [6]]
    # print(tree)
    # print(X, Y)
    # X, Y = 0, 3
    # tree = [[1], [0, 2, 3], [1, 4, 5], [1], [2], [2], [6]]
    # print(tree)
    # print(X, Y)
    # X, Y = 0, 6
    # tree = [[1, 2], [0, 3, 4], [0, 5, 6], [1], [1], [2], [2]]
    # print(tree)
    # print(X, Y)
    # X, Y = 0, 5
    # tree = [[1, 2], [0, 3, 4], [0, 5, 6], [1], [1], [2], [2]]
    # print(tree)
    # print(X, Y)
    # X, Y = 0, 4
    # tree = [[1, 2], [0, 3, 4], [0, 5, 6], [1], [1], [2], [2]]
    # print(tree)
    # print(X, Y)
    # X, Y = 0, 1
    # tree = [[1, 2], [0, 3,

=======
Suggestion 4

def main():
    n,x,y = map(int,input().split())
    tree = [[] for i in range(n+1)]
    for i in range(n-1):
        u,v = map(int,input().split())
        tree[u].append(v)
        tree[v].append(u)
    res = []
    def dfs(x,y):
        if x == y:
            res.append(x)
            return True
        for i in tree[x]:
            if dfs(i,y):
                res.append(x)
                return True
    dfs(x,y)
    res.reverse()
    print(*res)

=======
Suggestion 5

def dfs(v, p):
    global ans
    ans.append(v)
    for u in G[v]:
        if u != p:
            dfs(u, v)
            ans.append(v)
            #print(ans)
            #print("v=%d"%v)
            #print("u=%d"%u)
            #print("p=%d"%p)
            #print("G[v]=")
            #print(G[v])
            #print("G[u]=")
            #print(G[u])
            #print("G[p]=")
            #print(G[p])
            #print("ans=")
            #print(ans)
            #print("ans[-1]=")
            #print(ans[-1])
            #print("ans[-2]=")
            #print(ans[-2])
            #print("ans[-3]=")
            #print(ans[-3])
            #print("ans[-4]=")
            #print(ans[-4])
            #print("ans[-5]=")
            #print(ans[-5])
            #print("ans[-6]=")
            #print(ans[-6])
            #print("ans[-7]=")
            #print(ans[-7])
            #print("ans[-8]=")
            #print(ans[-8])
            #print("ans[-9]=")
            #print(ans[-9])
            #print("ans[-10]=")
            #print(ans[-10])
            #print("ans[-11]=")
            #print(ans[-11])
            #print("ans[-12]=")
            #print(ans[-12])
            #print("ans[-13]=")
            #print(ans[-13])
            #print("ans[-14]=")
            #print(ans[-14])
            #print("ans[-15]=")
            #print(ans[-15])
            #print("ans[-16]=")
            #print(ans[-16])
            #print("ans[-17]=")
            #print(ans[-17])
            #print("ans[-18]=")
            #print(ans[-18])
            #print("ans[-19]=")
            #print(ans[-19])
            #print("ans[-20]=")
            #print(ans[-20])
            #print("ans[-21]=")
            #print(ans[-21])
            #print("ans[-22]=")
            #print(ans[-22])
            #print("ans[-23]=")
            #print(ans[-23])
            #print("ans

=======
Suggestion 6

def dfs(v):
    global path
    global visited
    global G
    global N
    global X
    global Y
    global flag
    if flag == 1:
        return
    path.append(v)
    visited[v] = True
    if v == Y:
        flag = 1
        for i in path:
            print(i,end=' ')
        return
    for next_v in G[v]:
        if visited[next_v] == False:
            dfs(next_v)
            path.pop()

N,X,Y = map(int,input().split())
X -= 1
Y -= 1
G = [[] for i in range(N)]
for i in range(N-1):
    u,v = map(int,input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)
visited = [False]*N
path = []
flag = 0
dfs(X)

=======
Suggestion 7

def main():
    N, X, Y = map(int, input().split())
    graph = [[] for _ in range(N)]
    for i in range(N-1):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    #print(graph)
    #print(X, Y)
    #print(graph[X-1])
    #print(graph[Y-1])
    for i in range(N):
        if X-1 in graph[i]:
            #print(i)
            if Y-1 in graph[i]:
                print(i+1, end=' ')
                print(X, end=' ')
                print(Y, end=' ')
                break
            else:
                print(i+1, end=' ')
                print(X, end=' ')
                break
    for i in range(N):
        if Y-1 in graph[i]:
            if X-1 in graph[i]:
                break
            else:
                print(Y, end=' ')
                break
    print()

=======
Suggestion 8

def solve():
    # 树的节点数
    N = int(input())
    # 起点
    X = int(input())
    # 终点
    Y = int(input())
    # 边
    edges = []
    for i in range(N-1):
        edges.append(list(map(int, input().split())))
    # 顶点
    vertexs = []
    for i in range(N):
        vertexs.append([])

    # 顶点的子节点
    for edge in edges:
        vertexs[edge[0]-1].append(edge[1])
        vertexs[edge[1]-1].append(edge[0])

    # 顶点的父节点
    parents = [0] * N
    # 父节点的栈
    stack = []
    stack.append(1)
    while len(stack) > 0:
        vertex = stack.pop()
        for child in vertexs[vertex-1]:
            if child != parents[vertex-1]:
                parents[child-1] = vertex
                stack.append(child)

    # 起点到终点的路径
    path = []
    path.append(Y)
    while path[-1] != X:
        path.append(parents[path[-1]-1])

    # 输出
    for i in range(len(path)):
        print(path[len(path)-1-i], end=" ")
    print()

=======
Suggestion 9

def main():
    N,X,Y = map(int,input().split())
    U = [0]*(N-1)
    V = [0]*(N-1)
    for i in range(N-1):
        U[i],V[i] = map(int,input().split())
    #print(N,X,Y)
    #print(U,V)
    #print("-----")
    
    #树形结构
    tree = [[] for i in range(N+1)]
    for i in range(N-1):
        tree[U[i]].append(V[i])
        tree[V[i]].append(U[i])
    #print(tree)
    
    #深度优先搜索
    #print("深度优先搜索")
    #print("-----")
    #print("从顶点X到顶点Y的简单路径上的所有顶点的索引")
    #print("中间有空格")
    #print("-----")
    ans = []
    def dfs(now,pre):
        if now == Y:
            ans.append(now)
            return True
        for next in tree[now]:
            if next == pre:
                continue
            if dfs(next,now):
                ans.append(now)
                return True
        return False
    dfs(X,-1)
    ans = ans[::-1]
    print(" ".join(map(str,ans)))

=======
Suggestion 10

def dfs(u,p):
    global ans
    ans.append(u)
    for v in G[u]:
        if v!=p:
            dfs(v,u)
            ans.append(u)

n,x,y=map(int,input().split())
x-=1
y-=1
G=[[] for _ in range(n)]
for _ in range(n-1):
    u,v=map(int,input().split())
    u-=1
    v-=1
    G[u].append(v)
    G[v].append(u)
ans=[]
dfs(x,-1)
ans.append(y)
print(*[i+1 for i in ans])
