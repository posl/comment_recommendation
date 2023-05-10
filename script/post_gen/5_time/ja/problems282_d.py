Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in ra

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(lambda x: int(x) - 1, input().split())
        G[u].append(v)
        G[v].append(u)

    # 二部グラフ判定
    color = [-1] * N
    color[0] = 0
    q = [0]
    while q:
        u = q.pop()
        for v in G[u]:
            if color[v] == -1:
                color[v] = 1 - color[u]
                q.append(v)

    # 二部グラフならば、色が異なる頂点同士の辺の個数を数える
    if all(color[v] != -1 for v in range(N)):
        ans = sum(len(G[u]) for u in range(N)) // 2
        for u in range(N):
            for v in G[u]:
                if color[u] == color[v]:
                    ans -= 1
        ans //= 2
        print(ans)
    else:
        print(N * (N - 1) // 2 - M)

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    uv = [list(map(int, input().split())) for _ in range(m)]
    print(n, m)
    print(uv)

=======
Suggestion 4

def main():
    n,m = map(int,input().split())
    u = []
    v = []
    for i in range(m):
        u_,v_ = map(int,input().split())
        u.append(u_)
        v.append(v_)
    g = [[] for i in range(n+1)]
    for i in range(m):
        g[u[i]].append(v[i])
        g[v[i]].append(u[i])
    c = [0]*(n+1)
    for i in range(1,n+1):
        if c[i] == 0:
            c[i] = 1
            q = [i]
            while q:
                a = q.pop()
                for b in g[a]:
                    if c[b] == 0:
                        c[b] = -c[a]
                        q.append(b)
                    else:
                        if c[b] == c[a]:
                            print(0)
                            exit()
    ans = 0
    for i in range(1,n+1):
        if c[i] == 1:
            ans += 1
    print(ans*(n-ans)-m)
main()

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    #print(N, M)
    edge_list = [list(map(int, input().split())) for _ in range(M)]
    #print(edge_list)
    #print(len(edge_list))
    #print(edge_list[0])
    #print(edge_list[0][0])
    #print(edge_list[0][1])
    #print(len(edge_list[0]))
    #print(edge_list[0][0]-1)
    #print(edge_list[0][1]-1)

    # N個の頂点と M本の辺からなる単純な無向グラフGがある
    # i=1,2,...,Mについて、i番目の辺は頂点u_iと頂点v_iを結ぶ
    # 1 ≦ u < v ≦ Nを満たす整数の組(u,v)であって、
    # 2つの条件をともに満たすものの個数を出力

    # 1. グラフGにおいて、頂点uと頂点vを結ぶ辺は存在しない
    # 2. グラフGに、頂点uと頂点vを結ぶ辺を追加して得られるグラフは二部グラフである

    # 二部グラフとは？
    # 無向グラフが二部グラフであるとは、
    # 各頂点を黒または白のどちらかの色で塗ることができることを言います。
    # 同じ色に塗られた頂点どうしを結ぶ辺は存在しない。

    # 二部グラフであるかどうかを判定する
    # 1. 頂点の色を塗る
    # 2. 同じ色に塗られた頂点どうしを結ぶ辺が存在するかを

=======
Suggestion 6

def dfs(v, color):
    colors[v] = color
    for i in G[v]:
        if colors[i] == color:
            return False
        if colors[i] == 0 and not dfs(i, -color):
            return False
    return True

N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

colors = [0]*N
ans = 0
for i in range(N):
    if colors[i] == 0:
        if dfs(i, 1):
            ans += 1
print(ans)

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)
    color = [0] * (n + 1)
    def dfs(v, c):
        color[v] = c
        for to in g[v]:
            if color[to] == c:
                return False
            if color[to] == 0 and not dfs(to, -c):
                return False
        return True
    ans = 0
    for i in range(1, n + 1):
        if color[i] == 0:
            if dfs(i, 1):
                black = color.count(1)
                white = color.count(-1)
                ans += black * white
            else:
                break
    else:
        print(ans)
        return
    print(0)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for i in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    ans = 0
    for i in range(1, N+1):
        for j in graph[i]:
            if i < j:
                cnt = 0
                for k in graph[i]:
                    if k in graph[j]:
                        cnt += 1
                if cnt == 1:
                    ans += 1
    print(ans)

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    g = [[] for _ in range(n)]
    for i in range(m):
        a,b = map(int,input().split())
        g[a-1].append(b-1)
        g[b-1].append(a-1)

    color = [-1]*n
    def dfs(v,c):
        color[v] = c
        for i in g[v]:
            if color[i] == c:
                return False
            if color[i] == -1 and not dfs(i,1-c):
                return False
        return True

    ans = 0
    for i in range(n):
        if color[i] == -1:
            if dfs(i,1):
                ans += 1
    print(ans*(ans-1)//2-m+ans)
main()

=======
Suggestion 10

def dfs(v, c):
    color[v] = c
    for i in g[v]:
        if color[i] == c:
            return False
        if color[i] == 0 and not dfs(i, -c):
            return False
    return True

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)
color = [0]*n
ans = 0
for i in range(n):
    if color[i] == 0:
        if dfs(i, 1):
            ans += 1
print(ans)
