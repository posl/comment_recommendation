Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, q = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n - 1)]
    cd = [list(map(int, input().split())) for _ in range(q)]
    # 隣接リスト
    adj = [[] for _ in range(n)]
    for a, b in ab:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    # 深さ
    depth = [-1] * n
    depth[0] = 0
    # 幅優先探索
    que = [0]
    while que:
        v = que.pop(0)
        for nv in adj[v]:
            if depth[nv] == -1:
                depth[nv] = depth[v] + 1
                que.append(nv)
    # 二人の深さが同じならTown
    for c, d in cd:
        if depth[c - 1] == depth[d - 1]:
            print('Town')
        else:
            print('Road')

=======
Suggestion 2

def main():
    N,Q=map(int,input().split())
    G=[[] for i in range(N+1)]
    for i in range(N-1):
        a,b=map(int,input().split())
        G[a].append(b)
        G[b].append(a)
    #print(G)
    #print(N,Q)
    #p

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    AB = [map(int, input().split()) for _ in range(N-1)]
    CD = [map(int, input().split()) for _ in range(Q)]
    a, b = [list(i) for i in zip(*AB)]
    c, d = [list(i) for i in zip(*CD)]
    # 隣接リストを作成
    G = [[] for _ in range(N+1)]
    for i in range(N-1):
        G[a[i]].append(b[i])
        G[b[i]].append(a[i])
    # 頂点 1 からの距離を BFS で求める
    dist = [-1]*(N+1)
    dist[1] = 0
    que = [1]
    while que:
        v = que.pop()
        for nv in G[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v]+1
            que.append(nv)
    # 各クエリについて答える
    for i in range(Q):
        if (dist[c[i]]+dist[d[i]]) % 2 == 0:
            print("Town")
        else:
            print("Road")

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    ABC = [list(map(int, input().split())) for _ in range(N-1)]
    CD = [list(map(int, input().split())) for _ in range(Q)]

    # 隣接リスト
    G = [[] for _ in range(N+1)]
    for a, b in ABC:
        G[a].append(b)
        G[b].append(a)

    # 木の直径
    # 1 から最も遠い頂点を求める
    dis = [-1]*(N+1)
    dis[1] = 0
    stack = [1]
    while stack:
        v = stack.pop()
        for w in G[v]:
            if dis[w] == -1:
                dis[w] = dis[v] + 1
                stack.append(w)
    # 最も遠い頂点から最も遠い頂点までの距離を求める
    max_dis = max(dis)
    farthest = dis.index(max_dis)
    dis = [-1]*(N+1)
    dis[farthest] = 0
    stack = [farthest]
    while stack:
        v = stack.pop()
        for w in G[v]:
            if dis[w] == -1:
                dis[w] = dis[v] + 1
                stack.append(w)
    D = max(dis)

    # 木の直径の頂点を根とする二分木を作る
    # 木の直径を根とする二分木の深さは D+1 となる
    # 木の直径の頂点を根とする二分木の頂点の深さを求める
    dis = [-1]*(N+1)
    dis[farthest] = 0
    stack = [farthest]
    while stack:
        v = stack.pop()
        for w in G[v]:
            if dis[w] == -1:
                dis[w] = dis[v] + 1
                stack.append(w)

    # 木の直径の頂点を根とする二分木の各頂点の親を求める

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    # 隣接リスト
    adj = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    # 隣接行列
    #adj = [[0] * N for _ in range(N)]
    #for _ in range(N - 1):
    #    a, b = map(int, input().split())
    #    adj[a - 1][b - 1] = 1
    #    adj[b - 1][a - 1] = 1

    # 高橋君の街
    C = [0] * Q
    # 青木君の街
    D = [0] * Q
    for i in range(Q):
        c, d = map(int, input().split())
        C[i] = c - 1
        D[i] = d - 1

    # 高橋君の街からの距離
    dist =

=======
Suggestion 6

def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    edges = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        edges[a - 1].append(b - 1)
        edges[b - 1].append(a - 1)
    dist = [0] * N
    que = deque([0])
    while que:
        p = que.popleft()
        for c in edges[p]:
            if dist[c] == 0:
                dist[c] = dist[p] + 1
                que.append(c)
    for _ in range(Q):
        c, d = map(int, input().split())
        if (dist[c - 1] + dist[d - 1]) % 2 == 0:
            print("Town")
        else:
            print("Road")

=======
Suggestion 7

def main():
    N,Q = map(int,input().split())
    # 隣接リスト
    adj = [[] for _ in range(N)]
    for _ in range(N-1):
        a,b = map(int,input().split())
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
    # 各頂点の深さ
    depth = [-1]*N
    # 各頂点の親
    parent = [-1]*N
    # 各頂点の子
    children = [[] for _ in range(N)]
    # 0 を親とする木を作成
    depth[0] = 0
    parent[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for u in adj[v]:
            if depth[u] != -1:
                continue
            depth[u] = depth[v] + 1
            parent[u] = v
            children[v].append(u)
            stack.append(u)
    # 各頂点の部分木のサイズ
    size = [0]*N
    for v in reversed(range(N)):
        size[v] = 1
        for u in children[v]:
            size[v] += size[u]
    # 各頂点の部分木の根
    root = [0]*N
    for v in range(N):
        if v == 0 or len(children[parent[v]]) == 1:
            root[v] = v
        else:
            root[v] = root[parent[v]]
    # 各頂点の部分木の先頭
    head = [0]*N
    for v in range(N):
        if v == 0 or len(children[parent[v]]) == 1:
            head[v] = v
        else:
            head[v] = head[parent[v]]
    # 各頂点の部分木の先頭の深さ
    head_depth = [0]*N
    for v in range(N):
        if v == 0 or len(children[parent[v]]) == 1:
            head_depth[v] = depth[v]
        else:
            head_depth[v] = head_depth[parent[v]]
    # 各頂点の部分

=======
Suggestion 8

def main():
    # 入力
    N,Q = map(int,input().split())
    # 隣接リスト
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a,b = map(int,input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    # 根からの距離
    dist = [-1]*N
    dist[0] = 0
    # BFS
    que = [0]
    while que:
        v = que.pop()
        for u in G[v]:
            if dist[u] == -1:
                dist[u] = dist[v] + 1
                que.append(u)
    # 出力
    for _ in range(Q):
        c,d = map(int,input().split())
        if abs(dist[c-1]-dist[d-1])%2 == 0:
            print("Town")
        else:
            print("Road")

=======
Suggestion 9

def main():
    N, Q = map(int, input().split())
    # 隣接リスト
    graph = [[] for _ in range(N)]
    # 隣接リストに道路を追加
    for _ in range(N-1):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    # クエリを受け取る
    queries = [list(map(int, input().split())) for _ in range(Q)]
    # 高橋君の出発点
    start = [q[0] for q in queries]
    # 青木君の出発点
    goal = [q[1] for q in queries]
    # 道路の長さ
    length = [1] * (N-1)
    # 道路の長さを計算
    length = calc_length(graph, length)
    # クエリを処理
    for s, g in zip(start, goal):
        # 道路の長さの差が偶数ならTown、奇数ならRoad
        if (length[s-1] - length[g-1]) % 2 == 0:
            print("Town")
        else:
            print("Road")

=======
Suggestion 10

def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    def dfs(v, p=-1):
        d[v] = d[p] + 1
        for u in g[v]:
            if u == p:
                continue
            dfs(u, v)

    n, q = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)
    d = [0] * n
    dfs(0)
    for _ in range(q):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        if (d[c] + d[d]) % 2 == 0:
            print('Town')
        else:
            print('Road')
