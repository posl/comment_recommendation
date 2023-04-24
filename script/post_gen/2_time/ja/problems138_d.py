Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)
    #print(G)

    # 頂点1を根とする部分木に含まれる頂点の個数を求める
    # 1. 頂点1から順に深さ優先探索する
    # 2. 頂点1から順に、その頂点を根とする部分木に含まれる頂点の個数を求める
    # 3. 頂点1から順に、その頂点を根とする部分木に含まれる頂点の個数を累積和にする
    # 4. 頂点1から順に、その頂点を根とする部分木に含まれる頂点の個数を、その頂点を根とする部分木に含まれる頂点の個数の累積和にする
    # 5. 頂点1から順に、その頂点を根とする部分木に含まれる頂点の個数を、その頂点を根とする部分木に含まれる頂点の個数の累積和の累積和にする
    # 6. 各頂点のカウンターの値を求める

    # 1. 頂点1から順に深さ優先探索する
    # 2. 頂点1から順に、その頂点を根とする部分木に含まれる頂点の個数を求める
    # 3. 頂点1から順に、その頂点を根とする部

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    tree = [[] for _ in range(N)]

    for _ in range(N-1):
        a, b = map(int, input().split())
        tree[a-1].append(b-1)
        tree[b-1].append(a-1)

    #print(tree)
    #print()
    #print(tree[0])
    #print(tree[1])
    #print(tree[2])
    #print(tree[3])
    #print(tree[4])
    #print(tree[5])
    #print()

    #print("tree[0] = ", tree[0])
    #print("tree[1] = ", tree[1])
    #print("tree[2] = ", tree[2])
    #print("tree[3] = ", tree[3])
    #print("tree[4] = ", tree[4])
    #print("tree[5] = ", tree[5])

    #print("len(tree[0]) = ", len(tree[0]))
    #print("len(tree[1]) = ", len(tree[1]))
    #print("len(tree[2]) = ", len(tree[2]))
    #print("len(tree[3]) = ", len(tree[3]))
    #print("len(tree[4]) = ", len(tree[4]))
    #print("len(tree[5]) = ", len(tree[5]))

    #print("tree[0][0] = ", tree[0][0])
    #print("tree[0][1] = ", tree[0][1])
    #print("tree[1][0] = ", tree[1][0])
    #print("tree[2][0] = ", tree[2][0])
    #print("tree[3][0] = ", tree[3][0])
    #print("tree[4][0] = ", tree[4][0])
    #print("tree[5][0] = ", tree[5][0])

    #print("tree[0][0] = ", tree[0][0])
    #print("tree[0][1] = ", tree[0][1])
    #print("tree[1][0] = ", tree[1][0])
    #print("tree[2][0] = ", tree[2][0])

=======
Suggestion 3

def main():
    #入力
    N,Q = map(int,input().split())
    a = [0] * (N-1)
    b = [0] * (N-1)
    for i in range(N-1):
        a[i],b[i] = map(int,input().split())
    p = [0] * Q
    x = [0] * Q
    for i in range(Q):
        p[i],x[i] = map(int,input().split())
    #処理
    #頂点のカウンターの値
    c = [0] * N
    #隣接リスト
    G = [[] for i in range(N)]
    for i in range(N-1):
        G[a[i]-1].append(b[i]-1)
        G[b[i]-1].append(a[i]-1)
    #隣接リストを根から探索
    #根から隣接する頂点に x を足す
    #隣接する頂点からさらに隣接する頂点に x を足す
    #...
    #隣接する頂点に x を足す
    #隣接する頂点に x を足す
    #隣接する頂点に x を足す
    #...
    #隣接する頂点に x を足す
    #隣接する頂点に x を足す
    #隣接する頂点に x を足す
    #...
    #隣接する頂点に x を足す
    #隣接する頂点に x を足す
    #隣接する頂点に x を足す
    #...
    #隣接する頂点に x を足す
    #隣接する頂点に x を足す
    #隣接する頂点に x を足す
    #...
    #隣接する頂点に x を足す
    #隣接する頂点に x を足す
    #隣接する頂点に x を足

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    # 隣接リスト
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    # 木の根
    root = 0
    # 頂点iを根とする部分木の頂点数
    size = [0] * N
    # 頂点iの親
    parent = [0] * N
    # 頂点iの深さ
    depth = [0] * N
    # DFS
    def dfs(v, p, d):
        size[v] = 1
        parent[v] = p
        depth[v] = d
        for nv in G[v]:
            if nv == p:
                continue
            dfs(nv, v, d+1)
            size[v] += size[nv]
    dfs(root, -1, 0)
    # 頂点iの部分木に含まれる頂点のリスト
    subtree = [[] for _ in range(N)]
    for i in range(N):
        subtree[parent[i]].append(i)
    # 頂点iの部分木に含まれる頂点のリスト
    subtree = [[] for _ in range(N)]
    for i in range(N):
        subtree[parent[i]].append(i)
    # 頂点iの部分木に含まれる頂点のリスト
    subtree = [[] for _ in range(N)]
    for i in range(N):
        subtree[parent[i]].append(i)
    # カウンター
    counter = [0] * N
    # クエリ
    for _ in range(Q):
        p, x = map(int, input().split())
        counter[p-1] += x
        counter[root] -= x
        for v in subtree[p-1]:
            counter[v] += x
    # DFS
    def dfs(v, p):
        for nv in G[v]:
            if nv == p:
                continue
            counter[nv] += counter[v]
            dfs

=======
Suggestion 5

def main():
    #入力
    N,Q = map(int,input().split())
    #隣接リスト
    adj = [[] for _ in range(N)]
    for _ in range(N-1):
        a,b = map(int,input().split())
        a,b = a-1,b-1
        adj[a].append(b)
        adj[b].append(a)
    #各頂点のカウンターの値
    counter = [0]*N
    for _ in range(Q):
        p,x = map(int,input().split())
        p = p-1
        counter[p] += x
    #深さ優先探索
    stack = [0]
    visited = [False]*N
    while stack:
        v = stack.pop()
        visited[v] = True
        for w in adj[v]:
            if visited[w]:
                continue
            counter[w] += counter[v]
            stack.append(w)
    #出力
    print(" ".join(map(str,counter)))

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    # 木の構築
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    # 各頂点のカウンターの値
    C = [0] * N
    # 各操作
    for _ in range(Q):
        p, x = map(int, input().split())
        C[p-1] += x
    # 根から順にカウンターの値を伝搬
    q = [0]
    while q:
        v = q.pop()
        for w in G[v]:
            if C[w] == 0:
                C[w] = C[v]
                q.append(w)
    # 出力
    print(" ".join(map(str, C)))

=======
Suggestion 7

def main():
    from sys import stdin
    from collections import defaultdict
    def input(): return stdin.readline().strip()

    N, Q = map(int, input().split())
    edges = defaultdict(list)
    for i in range(N - 1):
        a, b = map(int, input().split())
        edges[a].append(b)
        edges[b].append(a)
    cnt = [0] * (N + 1)
    for i in range(Q):
        p, x = map(int, input().split())
        cnt[p] += x
    ans = [0] * (N + 1)
    def dfs(v, p):
        for u in edges[v]:
            if u == p: continue
            dfs(u, v)
            cnt[v] += cnt[u]
    dfs(1, -1)
    print(*cnt[1:])

=======
Suggestion 8

def main():
    N, Q = map(int, input().split())

    # a, bを入力
    ab = []
    for i in range(N-1):
        ab.append(list(map(int, input().split())))
    #print(ab)

    # p, xを入力
    px = []
    for i in range(Q):
        px.append(list(map(int, input().split())))
    #print(px)

    # リストの初期化
    ans = [0] * (N+1)
    #print(ans)

    # p, xのリストを作成
    for i in range(Q):
        ans[px[i][0]] += px[i][1]
        #print(ans)
    #print(ans)

    # a, bのリストを作成
    for i in range(N-1):
        ans[ab[i][1]] += ans[ab[i][0]]
        #print(ans)
    #print(ans)

    # 出力
    for i in range(1, N+1):
        print(ans[i], end=" ")
    print("")

=======
Suggestion 9

def main():
    N, Q = map(int, input().split())
    # 木を隣接リストで表現する
    # adj[i]: 頂点iの隣接頂点のリスト
    adj = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
    # 各頂点の親を記録する
    # par[i]: 頂点iの親
    par = [-1]*N
    # 各頂点の深さを記録する
    # depth[i]: 頂点iの深さ
    depth = [0]*N
    # 根からの距離を記録する
    # dist[i]: 根から頂点iまでの距離
    dist = [0]*N
    # 各頂点の子を記録する
    # children[i]: 頂点iの子のリスト
    children = [[] for _ in range(N)]
    # 親を記録しながら幅優先探索で木を辿る
    q = [0]
    while q:
        v = q.pop(0)
        for w in adj[v]:
            if par[v] != w:
                par[w] = v
                depth[w] = depth[v] + 1
                dist[w] = dist[v] + 1
                children[v].append(w)
                q.append(w)
    # 各頂点のカウンターの値を記録する
    # counter[i]: 頂点iのカウンターの値
    counter = [0]*N
    # 各操作のあとのカウンターの値を記録する
    # counter[i]: 頂点iのカウンターの値
    ans = [0]*N
    # 各操作を処理する
    for _ in range(Q):
        p, x = map(int, input

=======
Suggestion 10

def main():
    N, Q = map(int, input().split())
    # N:頂点数, Q:操作数
