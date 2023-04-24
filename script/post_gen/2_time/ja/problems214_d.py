Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        G[u - 1].append((v - 1, w))
        G[v - 1].append((u - 1, w))
    # print(G)

    # 頂点 0 を根として木を DFS する
    # 親から子への辺を辿る際に、その辺の重みを親の部分木のサイズとして記録しておく
    # 子から親への辺を辿る際に、その辺の重みを子の部分木のサイズとして記録しておく
    def dfs(v, p):
        for u, w in G[v]:
            if u == p:
                continue
            dfs(u, v)
            size[v] += size[u]
            ans[v] += ans[u] + size[u] * w

    size = [1] * N
    ans = [0] * N
    dfs(0, -1)

    # 頂点 0 を根として木を DFS する
    # 親から子への辺を辿る際に、その辺の重みを親の部分木のサイズとして記録しておく
    # 子から親への辺を辿る際に、その辺の重みを子の部分木のサイズとして記録しておく
    def dfs(v, p):
        for u, w in G[v]:
            if u == p:
                continue
            ans[u] = ans[v] + (N - size[u]) * w - size[u] * w
            dfs(u, v)

    dfs(0, -1)

    print(sum(ans))

=======
Suggestion 2

def main():
    N = int(input())
    graph = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        graph[u-1].append((v-1, w))
        graph[v-1].append((u-1, w))
    #print(graph)

    # 1. 任意の頂点を根とする
    # 2. 根から深さ優先探索で木を構築する
    # 3. 構築した木の葉から根へ向かって、葉から根への最短距離を求める
    # 4. 3で求めた最短距離を用いて、任意の2頂点間の最短距離を求める

    # 2. 根から深さ優先探索で木を構築する
    # この時、親頂点の情報も取得しておく
    parent = [-1] * N
    stack = [0]
    while stack:
        v = stack.pop()
        for u, w in graph[v]:
            if parent[u] == -1:
                parent[u] = v
                stack.append(u)

    # 3. 構築した木の葉から根へ向かって、葉から根への最短距離を求める
    # この時、親頂点からの重みも考慮して最短距離を求める
    # また、この最短距離を用いて、任意の2頂点間の最短距離を求める
    # この時、親頂点からの重みも考慮して最短距離を求める
    # また、この最短距離を用いて、任意の2頂点間

=======
Suggestion 3

def main():
    N = int(input())
    U = []
    V = []
    W = []
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        U.append(u)
        V.append(v)
        W.append(w)

    # 頂点1を根としたときの、各頂点の親を格納する配列
    parent = [-1] * (N + 1)
    # 各頂点の深さを格納する配列
    depth = [-1] * (N + 1)
    # 各頂点の重みの総和を格納する配列
    weight = [0] * (N + 1)

    # 隣接リストを作成
    edge = [[] for _ in range(N + 1)]
    for i in range(N - 1):
        edge[U[i]].append((V[i], W[i]))
        edge[V[i]].append((U[i], W[i]))

    # 木を幅優先探索で探索
    # 1を根とする
    parent[1] = 0
    depth[1] = 0
    q = [1]
    while q:
        v = q.pop(0)
        for nv, w in edge[v]:
            if parent[nv] != -1:
                continue
            parent[nv] = v
            depth[nv] = depth[v] + 1
            weight[nv] = weight[v] + w
            q.append(nv)

    # 各頂点の重みの総和の最大値を格納する配列
    max_weight = [0] * (N + 1)

    # 重みの総和の最大値を求める
    for i in range(N, 0, -1):
        max_weight[i] = max(max_weight[i], weight[i])
        max_weight[parent[i]] = max(max_weight[parent[i]], max_weight[i])

    # 各頂点の重みの総和の最大値の差を格納する配列
    diff_weight =

=======
Suggestion 4

def main():
    N = int(input())
    path = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        path[u - 1].append((v - 1, w))
        path[v - 1].append((u - 1, w))
    visited = [False] * N
    visited[0] = True
    stack = [(0, 0)]
    while stack:
        u, w = stack.pop()
        for v, w2 in path[u]:
            if visited[v]:
                continue
            visited[v] = True
            stack.append((v, w + w2))
    print(sum(w for w in visited) * (sum(visited) - 1))

=======
Suggestion 5

def main():
    N = int(input())
    f = [0] * N
    for i in range(N - 1):
        u, v, w = map(int, input().split())
        f[u - 1] += w
        f[v - 1] += w
    print(sum(f) // 2)

=======
Suggestion 6

def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        u,v,w = map(int,input().split())
        G[u-1].append((v-1,w))
        G[v-1].append((u-1,w))
    #print(G)
    #print(N)
    #print(G)
    #print(DFS(0,G))
    ans = 0
    for i in range(N):
        ans += DFS(i,G)[0]
    print(ans)

=======
Suggestion 7

def main():
    import sys
    sys.setrecursionlimit(10**6)
    input = sys.stdin.readline

    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        G[u - 1].append((v - 1, w))
        G[v - 1].append((u - 1, w))

    from collections import deque
    depth = [-1] * N
    depth[0] = 0
    q = deque([0])
    while q:
        v = q.popleft()
        for nv, w in G[v]:
            if depth[nv] == -1:
                depth[nv] = depth[v] + 1
                q.append(nv)

    # dp[v][k] := vの2^k親の頂点
    dp = [[-1] * 20 for _ in range(N)]
    dp[0][0] = 0
    for v in range(N):
        for k in range(19):
            if dp[v][k] == -1:
                break
            dp[v][k + 1] = dp[dp[v][k]][k]

    def lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        for k in range(20):
            if (depth[u] - depth[v]) & (1 << k):
                u = dp[u][k]
        if u == v:
            return u
        for k in range(19, -1, -1):
            if dp[u][k] != dp[v][k]:
                u = dp[u][k]
                v = dp[v][k]
        return dp[u][0]

    def dist(u, v):
        return depth[u] + depth[v] - 2 * depth[lca(u, v)]

    ans = 0
    for v in range(N):
        for nv, w in G[v]:
            if v < nv:
                ans += w * (N - dist(v, nv))

    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    #各頂点に隣接する頂点のリスト
    adjacent = [[] for _ in range(N)]
    #各頂点に隣接する辺の重みのリスト
    weight = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        adjacent[u - 1].append(v - 1)
        adjacent[v - 1].append(u - 1)
        weight[u - 1].append(w)
        weight[v - 1].append(w)

    #各頂点からの距離
    dist = [0] * N
    #各頂点からの距離を計算
    def calc_dist(v, p):
        for i, u in enumerate(adjacent[v]):
            if u == p:
                continue
            dist[u] = dist[v] + weight[v][i]
            calc_dist(u, v)
    calc_dist(0, -1)

    #各頂点の深さ
    depth = [0] * N
    #各頂点の深さを計算
    def calc_depth(v, p):
        for u in adjacent[v]:
            if u == p:
                continue
            depth[u] = depth[v] + 1
            calc_depth(u, v)
    calc_depth(0, -1)

    #各頂点に隣接する頂点のリスト
    adjacent2 = [[] for _ in range(N)]
    #各頂点に隣接する辺の重みのリスト
    weight2 = [[] for _ in range(N)]
    #各頂点に隣接する頂点のリストを作成
    for i in range(N):
        for j in range(len(adjacent[i])):
            if depth[adjacent[i][j]] > depth[i]:
                adjacent2[i].append(adjacent[i][j])
                weight2[i].append(weight[i][j])
    #print(adjacent2)
    #print(weight2)

    #各頂点に隣接する頂点のリスト
    adjacent3 = [[] for

=======
Suggestion 9

def main():
    N = int(input())
    edges = [list(map(int, input().split())) for _ in range(N - 1)]
    edges.sort(key=lambda x: x[2])

    # 頂点iからの距離の累積和
    # 重みの和
    dist = [0] * (N + 1)
    for u, v, w in edges:
        dist[u] += w
        dist[v] += w

    # 頂点iに対する、iに繋がる辺の重みの累積和
    # 重みの和
    cum_w = [0] * (N + 1)
    for u, v, w in edges:
        cum_w[u] += w
        cum_w[v] += w

    # 頂点iに対する、iに繋がる辺の重みの累積和
    # 重みの和
    cum_w = [0] * (N + 1)
    for u, v, w in edges:
        cum_w[u] += w
        cum_w[v] += w

    # 頂点iに対する、iに繋がる辺の重みの累積和
    # 重みの和
    cum_w = [0] * (N + 1)
    for u, v, w in edges:
        cum_w[u] += w
        cum_w[v] += w

    # 頂点iに対する、iに繋がる辺の重みの累積和
    # 重みの和
    cum_w = [0] * (N + 1)
    for u, v, w in edges:
        cum_w[u] += w
        cum_w[v] += w

    # 頂点iに対する、iに繋がる辺の重みの累積和
    # 重みの和
    cum_w = [0] * (N + 1)
    for u, v, w in edges:
        cum_w[u] += w
        cum_w[v] += w

=======
Suggestion 10

def main():
    N = int(input())
    # 隣接リスト
    adj_list = [[] for _ in range(N)]
    # 各辺の重み
    edge_weight = []
    # 各頂点の親
    parent = [-1] * N
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        adj_list[u].append((v, w))
        adj_list[v].append((u, w))
        edge_weight.append(w)
    # 各頂点の深さ
    depth = [0] * N
    # 各頂点の部分木の重みの和
    subtree_weight = [0] * N
    # 各頂点の部分木の重みの和を計算する
    def dfs(v):
        for u, w in adj_list[v]:
            if u != parent[v]:
                parent[u] = v
                depth[u] = depth[v] + 1
                dfs(u)
                subtree_weight[v] += subtree_weight[u] + w
    dfs(0)
    # 各頂点の部分木の重みの和を根に向かって伝播する
    def dfs2(v):
        for u, w in adj_list[v]:
            if u != parent[v]:
                subtree_weight[u] = subtree_weight[v] - w + (subtree_weight[0] - subtree_weight[u] - w)
                dfs2(u)
    dfs2(0)
    # 各辺の重みの和
    ans = sum(edge_weight)
    # 各頂点の部分木の重みの和の和
    ans += sum(subtree_weight)
    # 答えを出力する
    print(ans)
