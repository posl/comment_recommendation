Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N-1)]
    CD = [list(map(int, input().split())) for _ in range(Q)]

    # グラフの作成
    G = [[] for _ in range(N)]
    for a, b in AB:
        G[a-1].append(b-1)
        G[b-1].append(a-1)

    # 各頂点の深さを求める
    depth = [-1] * N
    depth[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for w in G[v]:
            if depth[w] == -1:
                depth[w] = depth[v] + 1
                stack.append(w)

    # 各頂点の親を求める
    parent = [-1] * N
    stack = [0]
    while stack:
        v = stack.pop()
        for w in G[v]:
            if parent[w] == -1:
                parent[w] = v
                stack.append(w)

    # 各クエリについて答える
    for c, d in CD:
        c -= 1
        d -= 1
        if depth[c] < depth[d]:
            c, d = d, c
        while depth[c] > depth[d]:
            c = parent[c]
        while c != d:
            c = parent[c]
            d = parent[d]
        if depth[c] % 2 == 0:
            print("Town")
        else:
            print("Road")

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    edges = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        edges[a-1].append(b-1)
        edges[b-1].append(a-1)

    def dfs(v, p, d):
        depth[v] = d
        for u in edges[v]:
            if u != p:
                dfs(u, v, d+1)

    depth = [0] * N
    dfs(0, -1, 0)

    for _ in range(Q):
        c, d = map(int, input().split())
        if (depth[c-1] + depth[d-1]) % 2 == 0:
            print('Town')
        else:
            print('Road')

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    edges = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        edges[a - 1].append(b - 1)
        edges[b - 1].append(a - 1)
    depth = [-1] * N
    depth[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for w in edges[v]:
            if depth[w] == -1:
                depth[w] = depth[v] + 1
                stack.append(w)
    for _ in range(Q):
        c, d = map(int, input().split())
        if (depth[c - 1] + depth[d - 1]) % 2 == 0:
            print("Town")
        else:
            print("Road")

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    edge = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        edge[a - 1].append(b - 1)
        edge[b - 1].append(a - 1)
    dist = [0] * N
    stack = [0]
    while stack:
        v = stack.pop()
        for u in edge[v]:
            if dist[u] == 0 and u != 0:
                dist[u] = dist[v] + 1
                stack.append(u)
    for _ in range(Q):
        c, d = map(int, input().split())
        if (dist[c - 1] + dist[d - 1]) % 2 == 0:
            print("Town")
        else:
            print("Road")

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    AB = []
    for i in range(N - 1):
        AB.append(list(map(int, input().split())))
    CD = []
    for i in range(Q):
        CD.append(list(map(int, input().split())))
    edges = [[] for i in range(N)]
    for i in range(N - 1):
        a, b = AB[i]
        edges[a - 1].append(b - 1)
        edges[b - 1].append(a - 1)
    depth = [0] * N
    parent = [0] * N
    parent[0] = -1
    q = [0]
    while len(q) > 0:
        v = q.pop()
        for i in edges[v]:
            if depth[i] == 0:
                depth[i] = depth[v] + 1
                parent[i] = v
                q.append(i)
    for c, d in CD:
        c -= 1
        d -= 1
        if (depth[c] + depth[d]) % 2 == 0:
            print("Town")
        else:
            print("Road")

=======
Suggestion 6

def main():
    import sys
    from collections import deque
    input = sys.stdin.readline

    N, Q = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)

    depth = [0]*N
    parent = [0]*N
    q = deque([0])
    while q:
        v = q.popleft()
        for w in G[v]:
            if depth[w] == 0:
                depth[w] = depth[v] + 1
                parent[w] = v
                q.append(w)

    for _ in range(Q):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        if depth[c] < depth[d]:
            c, d = d, c

        while depth[c] > depth[d]:
            c = parent[c]

        while c != d:
            c = parent[c]
            d = parent[d]

        if c == d:
            if depth[c] % 2 == 0:
                print("Town")
            else:
                print("Road")

=======
Suggestion 7

def main():
    N, Q = map(int, input().split())
    # 隣接リスト
    adj = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        adj[a].append(b)
        adj[b].append(a)
    # 頂点の深さ
    depth = [-1] * N
    depth[0] = 0
    # 頂点の親
    parent = [-1] * N
    # 深さ優先探索
    stack = [0]
    while stack:
        v = stack.pop()
        for u in adj[v]:
            if depth[u] == -1:
                depth[u] = depth[v] + 1
                parent[u] = v
                stack.append(u)
    # 各クエリについて
    for _ in range(Q):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        # 同じ深さにする
        while depth[c] > depth[d]:
            c = parent[c]
        while depth[d] > depth[c]:
            d = parent[d]
        # 共通の親を探す
        while c != d:
            c = parent[c]
            d = parent[d]
        # 答えを出力
        if depth[c] % 2 == 0:
            print('Town')
        else:
            print('Road')

=======
Suggestion 8

def main():
    N, Q = map(int, input().split())

    # 隣接リスト
    graph = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    # クエリ
    query = [list(map(int, input().split())) for _ in range(Q)]

    # 隣接リストを隣接行列に変換
    adj = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in graph[i]:
            adj[i][j] = 1

    # 1からの距離を求める
    dist = [0] * N
    stack = [0]
    while stack:
        i = stack.pop()
        for j in graph[i]:
            if dist[j] == 0:
                dist[j] = dist[i] + 1
                stack.append(j)

    # クエリを処理
    for c, d in query:
        if dist[c-1] % 2 == dist[d-1] % 2:
            print('Town')
        else:
            print('Road')

=======
Suggestion 9

def dfs(v, p, d):
    depth[v] = d
    for u in graph[v]:
        if u == p:
            continue
        dfs(u, v, d + 1)

=======
Suggestion 10

def main():
    N, Q = map(int, input().split())
    # 各頂点について、その頂点からの距離を記録する
    distance = [-1] * N
    # 0番目の頂点は、0番目の頂点からの距離は0
    distance[0] = 0
    # 隣接リストを用意する
    edges = [[] for _ in range(N)]
    # 隣接リストに、各頂点の隣接する頂点を格納していく
    for _ in range(N-1):
        a, b = map(int, input().split())
        edges[a-1].append(b-1)
        edges[b-1].append(a-1)
    # 幅優先探索で、各頂点からの距離を計算する
    queue = [0]
    while queue:
        # 今いる頂点を取り出す
        now = queue.pop(0)
        # 今いる頂点から隣接する頂点を取り出していく
        for edge in edges[now]:
            # すでに距離が計算されている頂点はスキップする
            if distance[edge] != -1:
                continue
            # 距離を計算する
            distance[edge] = distance[now] + 1
            # 計算した頂点をqueueに追加する
            queue.append(edge)
    # 各クエリについて処理を行う
    for _ in range(Q):
        c, d = map(int, input().split())
        # cとdの距離が偶数なら、Townに到着する
        if (distance[c-1] + distance[d-1]) % 2 == 0:
            print('Town')
        # cとdの距離が奇数なら、Roadに到着する
        else:
            print('Road')
