Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N = int(input())
    edges = []
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))

    edges.sort()

    ans = 0
    for w, u, v in edges:
        ans += w * min(u, v) * (N - max(u, v) + 1)
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    edges = []
    for i in range(n-1):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    ans = 0
    for u, v, w in edges:
        ans += uf.size(u) * uf.size(v) * w
        uf.unite(u, v)
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        u,v,w = map(int,input().split())
        G[u-1].append((v-1,w))
        G[v-1].append((u-1,w))

    def dfs(v,p):
        for nv,w in G[v]:
            if nv == p:
                continue
            dist[nv] = dist[v] + w
            dfs(nv,v)

    dist = [0]*N
    dfs(0,-1)

    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            ans += max(dist[i],dist[j])

    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    tree = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        tree[u - 1].append((v - 1, w))
        tree[v - 1].append((u - 1, w))
    #print(tree)
    #print(tree[0])
    #print(tree[1])
    #print(tree[2])
    #print(tree[3])
    #print(tree[4])
    
    #1からの距離を求める
    dist1 = [0] * N
    dist1[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for u, w in tree[v]:
            if dist1[u] == 0:
                dist1[u] = dist1[v] + w
                stack.append(u)
    #print(dist1)
    
    #Nからの距離を求める
    dist2 = [0] * N
    dist2[N - 1] = 0
    stack = [N - 1]
    while stack:
        v = stack.pop()
        for u, w in tree[v]:
            if dist2[u] == 0:
                dist2[u] = dist2[v] + w
                stack.append(u)
    #print(dist2)
    
    #1からの距離とNからの距離の差を求める
    dist3 = []
    for i in range(N):
        dist3.append(dist2[i] - dist1[i])
    #print(dist3)
    
    #1からの距離とNからの距離の差の絶対値の合計を求める
    dist4 = sum(list(map(abs, dist3)))
    #print(dist4)
    
    #1からの距離とNからの距離の差の絶対値の合計と1からの距離とNからの距離の差の絶対値の合計の差の合計を求める
    dist5 = sum(list(map(abs, dist3

=======
Suggestion 5

def main():
    n = int(input())
    uvw = []
    for i in range(n-1):
        uvw.append(list(map(int,input().split())))
    print(uvw)
    # n = 3
    # uvw = [[1, 2, 10], [2, 3, 20]]
    # n = 5
    # uvw = [[1, 2, 1], [2, 3, 2], [4, 2, 5], [3, 5, 14]]

    # 木の頂点の数
    N = n
    # 木の辺の数
    M = n-1
    # 頂点の数
    V = N
    # 辺の数
    E = M
    # 頂点の最大数
    MAX_V = 100000
    # 辺の最大数
    MAX_E = 100000

    # グラフ
    G = [[0 for i in range(MAX_V)] for j in range(MAX_E)]
    # 重み
    W = [[0 for i in range(MAX_V)] for j in range(MAX_E)]

    # グラフの初期化
    def graph_init():
        for i in range(MAX_V):
            for j in range(MAX_V):
                G[i][j] = 0

    # 辺の追加
    def add_edge(a, b, w):
        G[a].append(b)
        W[a].append(w)

    # BFS
    def bfs(s):
        global d
        global p
        global color
        for i in range(MAX_V):
            d[i] = float('inf')
            p[i] = -1
        q = []
        q.append(s)
        d[s] = 0
        color[s] = 1
        while len(q) != 0:
            u = q.pop(0)
            for i in range(len(G[u])):
                v = G[u][i]
                if color[v] == 0:
                    color[v] = 1
                    d[v] = d[u] + 1
                    p[v] = u
                    q.append(v)
            color[u] = 2

    # 最短経路

=======
Suggestion 6

def main():
    N = int(input())
    edges = []
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    edges.sort(key=lambda x: x[2], reverse=True)
    uf = UnionFind(N)
    ans = 0
    for u, v, w in edges:
        ans += uf.size(u) * uf.size(v) * w
        uf.union(u, v)
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n-1)]
    edges.sort(key=lambda x: x[2])
    ans = 0
    for i in range(n-1):
        ans += edges[i][2] * (i+1) * (n-i-1)
    print(ans)

=======
Suggestion 8

def dfs(G, v, p, d, D):
    D[v] = d
    for w in G[v]:
        if w != p:
            dfs(G, w, v, d + 1, D)

=======
Suggestion 9

def main():
    n = int(input())
    uvw = [list(map(int, input().split())) for _ in range(n - 1)]
    g = [[] for _ in range(n)]
    for u, v, w in uvw:
        g[u - 1].append((v - 1, w))
        g[v - 1].append((u - 1, w))

    def dfs(u, p = -1):
        res = 0
        for v, w in g[u]:
            if v == p:
                continue
            res = max(res, dfs(v, u) + w)
        return res

    ans = 0
    for u in range(n):
        ans = max(ans, dfs(u))
    print(ans * 2)

=======
Suggestion 10

def main():
    N = int(input())
    uvw_list = []
    for i in range(N-1):
        uvw_list.append(list(map(int, input().split())))
    print(uvw_list)
