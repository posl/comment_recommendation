Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N,X,Y = map(int,input().split())
    print(N,X,Y)
    for i in range(N-1):
        U,V = map(int,input().split())
        print(U,V)

=======
Suggestion 2

def dfs(now, prev):
    if now == y:
        print(now, end=" ")
        return True
    for to in edge[now]:
        if to == prev:
            continue
        if dfs(to, now):
            print(now, end=" ")
            return True
    return False

n, x, y = map(int, input().split())
x -= 1
y -= 1
edge = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edge[u].append(v)
    edge[v].append(u)
dfs(x, -1)

=======
Suggestion 3

def dfs(v, p):
    global g
    global ans
    ans.append(v)
    for u in g[v]:
        if u != p:
            dfs(u, v)
            ans.append(v)

n, x, y = map(int, input().split())
g = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
ans = []
dfs(x, 0)
print(*ans)

=======
Suggestion 4

def main():
    N, X, Y = map(int, input().split())
    U = []
    V = []
    for i in range(N-1):
        u, v = map(int, input().split())
        U.append(u)
        V.append(v)
    print(U, V)

=======
Suggestion 5

def dfs(v, p):
    global ans
    ans.append(v)
    for u in g[v]:
        if u != p:
            dfs(u, v)
            ans.append(v)

n, x, y = map(int, input().split())
g = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

ans = []
dfs(x, -1)
print(*ans)

=======
Suggestion 6

def main():
    # 读取输入
    n, x, y = map(int, input().split())
    uv = [list(map(int, input().split())) for _ in range(n-1)]
    # 构建邻接表
    adj = [[] for _ in range(n+1)]
    for u, v in uv:
        adj[u].append(v)
        adj[v].append(u)

    # DFS
    def dfs(u, p):
        for v in adj[u]:
            if v == p:
                continue
            if v == y:
                return [v]
            res = dfs(v, u)
            if res:
                return [u] + res
        return []

    res = dfs(x, -1)
    print(*res)

=======
Suggestion 7

def dfs(v, p):
    global ans
    ans.append(v)
    for i in G[v]:
        if i != p:
            dfs(i, v)
            ans.append(v)

N, X, Y = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

ans = []
dfs(X, -1)
ans.append(X)
ans.reverse()
ans.pop()
dfs(Y, -1)
ans.append(Y)
print(*ans)

=======
Suggestion 8

def main():
    n, x, y = map(int, input().split())
    uv = [list(map(int, input().split())) for _ in range(n - 1)]
    print(uv)
    # ここにコードを追記
    # 1 から各頂点への最短距離を求める
    # 1 から x, y への最短距離を求める
    # x, y から各頂点への最短距離を求める
    # 1 から x までの最短距離 + 1 + y から各頂点への最短距離
    # 1 から y までの最短距離 + 1 + x から各頂点への最短距離
    # これらの最小値が答え

=======
Suggestion 9

def dfs(v,p):
    global ans
    ans.append(v)
    for u in G[v]:
        if u != p:
            dfs(u,v)
            ans.append(v)
    return

N,X,Y = map(int,input().split())
U = [0]*(N-1)
V = [0]*(N-1)
for i in range(N-1):
    U[i],V[i] = map(int,input().split())
G = [[] for _ in range(N+1)]
for i in range(N-1):
    G[U[i]].append(V[i])
    G[V[i]].append(U[i])
ans = []
dfs(X,-1)
ans.append(X)
ans.reverse()
ans.append(Y)
print(*ans)

=======
Suggestion 10

def dfs(x, p):
    global ans
    ans.append(x)
    for y in G[x]:
        if y != p:
            dfs(y, x)
            ans.append(x)
    return

N, X, Y = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

ans = []
dfs(X, -1)
ans.append(X)
ans.reverse()
dfs(Y, -1)
print(*ans)
