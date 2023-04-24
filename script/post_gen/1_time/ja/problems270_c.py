Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    edge = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edge[u].append(v)
        edge[v].append(u)
    dist = [-1] * N
    dist[X] = 0
    que = [X]
    while que:
        v = que.pop()
        for u in edge[v]:
            if dist[u] != -1:
                continue
            dist[u] = dist[v] + 1
            que.append(u)
    ans = [0] * N
    for i, d in enumerate(dist):
        ans[d] += 1
    for i in range(1, N):
        if ans[i] == 0:
            break
        print(ans[i] // 2)

main()

=======
Suggestion 2

def main():
    N, X, Y = map(int, input().split())
    tree = [[] for i in range(N+1)]
    for i in range(N-1):
        U, V = map(int, input().split())
        tree[U].append(V)
        tree[V].append(U)
    X_to_Y = [0 for i in range(N+1)]
    Y_to_X = [0 for i in range(N+1)]
    X_to_Y[X] = 1
    Y_to_X[Y] = 1
    for i in range(1,N+1):
        if X_to_Y[i] == 1:
            for j in tree[i]:
                if X_to_Y[j] == 0:
                    X_to_Y[j] = X_to_Y[i] + 1
        if Y_to_X[i] == 1:
            for j in tree[i]:
                if Y_to_X[j] == 0:
                    Y_to_X[j] = Y_to_X[i] + 1
    for i in range(1,N+1):
        if X_to_Y[i] == 0:
            X_to_Y[i] = N+1
        if Y_to_X[i] == 0:
            Y_to_X[i] = N+1
    for i in range(1,N+1):
        if X_to_Y[i] < Y_to_X[i]:
            print(i, end = " ")
    print(Y)

main()

=======
Suggestion 3

def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    edge = [[] for _ in range(N)]
    for i in range(N-1):
        u, v = map(int, input().split())
        edge[u-1].append(v-1)
        edge[v-1].append(u-1)
    ans = [0] * N
    for i in range(N):
        if i == X:
            continue
        if i == Y:
            ans[i] = abs(i - X)
        else:
            ans[i] = bfs(i, X, Y, edge)
    for i in range(N):
        print(ans[i])

=======
Suggestion 4

def main():
    N,X,Y = map(int,input().split())
    X -= 1
    Y -= 1
    graph = [[] for _ in range(N)]
    for _ in range(N-1):
        a,b = map(int,input().split())
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)

    ans = [-1]*N
    ans[X] = 0
    queue = [X]
    while queue:
        v = queue.pop(0)
        for nv in graph[v]:
            if ans[nv] != -1:continue
            ans[nv] = ans[v] + 1
            queue.append(nv)
    print(*ans[Y:Y+1])

=======
Suggestion 5

def main():
    N,X,Y = map(int, input().split())
    X -= 1
    Y -= 1
    U = [0] * (N-1)
    V = [0] * (N-1)
    for i in range(N-1):
        U[i],V[i] = map(int, input().split())
        U[i] -= 1
        V[i] -= 1
    XtoY = [0] * N
    XtoY[X] = 1
    for i in range(N-1):
        if U[i] == X:
            XtoY[V[i]] = XtoY[U[i]] + 1
        elif V[i] == X:
            XtoY[U[i]] = XtoY[V[i]] + 1
        else:
            pass
    XtoY[Y] = 1
    for i in range(N-1):
        if U[i] == Y:
            XtoY[V[i]] = XtoY[U[i]] + 1
        elif V[i] == Y:
            XtoY[U[i]] = XtoY[V[i]] + 1
        else:
            pass
    for i in range(N):
        if XtoY[i] == 0:
            XtoY[i] = 1
        else:
            pass
    XtoY[X] = 0
    XtoY[Y] = 0
    for i in range(N):
        if XtoY[i] == 1:
            print(i+1,end=" ")
        else:
            pass

=======
Suggestion 6

def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    # 隣接リスト
    adj = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    # 頂点 x から頂点 y への単純パスを求める
    # 木のため、単純パスはただ一つ存在することが証明できる
    # 木上の任意の相異なる 2 頂点 a,b について、a から b への単純パスがただ一つ存在することが証明できます。
    # 頂点 x から頂点 y への単純パス上の頂点（端点含む）を順に列挙する
    # 頂点 x から頂点 y への単純パスを求める
    # 木のため、単純パスはただ一つ存在することが証明できる
    # 木上の任意の相異なる 2 頂点 a,b について、a から b への単純パスがただ一つ存在することが証明できます。
    # 頂点 x から頂点 y への単純パス上の頂点（端点含む）を順に列挙する
    # 頂点 x から頂点 y への単純パスを求める
    # 木のため、単純パスはただ一つ存在することが証明できる
    # 木上の任意の相異なる 2 頂点 a,b について、

=======
Suggestion 7

def main():
    N, X, Y = map(int, input().split())
    # 隣接リスト
    G = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    # 距離を格納するリスト
    dist = [-1] * (N + 1)
    # 幅優先探索
    dist[X] = 0
    q = [X]
    while q:
        v = q.pop(0)
        for nv in G[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            q.append(nv)
    # 出力
    for i in range(1, N + 1):
        if i == X:
            continue
        print(dist[i])

=======
Suggestion 8

def main():
    n, x, y = map(int, input().split())
    x -= 1
    y -= 1
    # 隣接リスト
    E = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        E[u].append(v)
        E[v].append(u)
    # 各頂点からの距離を格納する配列
    dist = [0] * n
    # 頂点 x からの距離を求める
    q = [x]
    while q:
        v = q.pop()
        for u in E[v]:
            if dist[u] == 0:
                dist[u] = dist[v] + 1
                q.append(u)
    # 頂点 y からの距離を求める
    q = [y]
    while q:
        v = q.pop()
        for u in E[v]:
            if dist[u] == 0:
                dist[u] = dist[v] + 1
                q.append(u)
    # 各距離の頂点数を求める
    ans = [0] * n
    for d in dist:
        ans[d] += 1
    # 頂点 x と頂点 y の距離は 0 なので、それを除く
    print(*ans[1:])

=======
Suggestion 9

def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    # グラフ部分
    graph = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    # 頂点 X から頂点 Y への単純パスを求める
    # まず頂点 X から頂点 Y へのパスを求める
    path = []
    stack = [X]
    while stack:
        v = stack.pop()
        path.append(v)
        if v == Y:
            break
        for u in graph[v]:
            if u not in path:
                stack.append(u)
    # 頂点 X から頂点 Y への単純パスを求める
    simple_path = [path[0]]
    for i in range(1, len(path)-1):
        if path[i-1] in graph[path[i]] and path[i+1] in graph[path[i]]:
            continue
        simple_path.append(path[i])
    simple_path.append(path[-1])
    print(*simple_path)

=======
Suggestion 10

def main():
    N, X, Y = map(int, input().split())
    # 木の辺の情報を格納するリスト
    edges = [[] for i in range(N + 1)]
    # 入力例1の場合
    # edges = [[], [2, 3], [1], [1, 4, 5], [3], [3]]
    # 入力例2の場合
    # edges = [[], [3, 2, 4], [1, 5, 6], [1], [1], [2], [2]]
    for i in range(N - 1):
        u, v = map(int, input().split())
        edges[u].append(v)
        edges[v].append(u)
    # 木の辺の情報を格納するリスト
    # edges = [[], [2, 3], [1, 5, 6], [1, 4], [3], [2], [2]]
    # 木の辺の情報を格納するリスト
    # edges = [[], [2, 3], [1, 5, 6], [1, 4], [3], [2], [2]]
    # 木の辺の情報を格納するリスト
    # edges = [[], [2, 3], [1, 5, 6], [1, 4], [3], [2], [2]]
    # 木の辺の情報を格納するリスト
    # edges = [[], [2, 3], [1, 5, 6], [1, 4], [3], [2], [2]]
    # 木の辺の情報を格納するリスト
    # edges = [[], [2, 3], [1, 5, 6], [1, 4], [3], [2], [2]]
    # 木の辺の情報を格納するリスト
    # edges = [[], [2, 3], [1, 5, 6], [1, 4], [3], [2], [2]]
    # 木の
