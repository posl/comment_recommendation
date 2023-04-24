Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    dist = [-1] * N
    dist[X] = 0
    queue = [X]
    while queue:
        v = queue.pop()
        for nv in graph[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            queue.append(nv)
    ans = [0] * N
    for i in range(N):
        if dist[i] == -1:
            continue
        ans[dist[i]] += 1
    for i in range(1, N):
        print(ans[i])

=======
Suggestion 2

def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    # print(graph)
    # print(X, Y)
    from collections import deque
    q = deque()
    q.append((X, 0))
    visited = [-1] * N
    visited[X] = 0
    while q:
        v, d = q.popleft()
        for nv in graph[v]:
            if visited[nv] == -1:
                visited[nv] = d + 1
                q.append((nv, d + 1))
    # print(visited)
    ans = [0] * N
    for i in range(N):
        if i != X:
            ans[visited[i]] += 1
    print(*ans[1:], sep=" ")

=======
Suggestion 3

def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    dist = [-1] * N
    dist[X] = 0
    stack = [X]
    while stack:
        v = stack.pop()
        for nv in graph[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                stack.append(nv)
    ans = [0] * N
    for i in range(N):
        if i == X:
            continue
        ans[dist[i]] += 1
    for i in range(1, N):
        print(ans[i])

=======
Suggestion 4

def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    tree = [[] for _ in range(N)]
    for _ in range(N-1):
        U, V = map(int, input().split())
        U -= 1
        V -= 1
        tree[U].append(V)
        tree[V].append(U)
    dist = [0] * N
    dist[X] = 1
    que = [X]
    while que:
        node = que.pop(0)
        for child in tree[node]:
            if dist[child] == 0:
                dist[child] = dist[node] + 1
                que.append(child)
    ans = []
    for i in range(N):
        if i == X or i == Y:
            continue
        if dist[i] == 0:
            continue
        if dist[i] == dist[Y] + 1:
            ans.append(i+1)
    print(*ans)

=======
Suggestion 5

def main():
    N,X,Y = map(int,input().split())
    X -= 1
    Y -= 1
    edge = [[] for _ in range(N)]
    for i in range(N-1):
        u,v = map(int,input().split())
        u -= 1
        v -= 1
        edge[u].append(v)
        edge[v].append(u)
    #print(edge)
    dist = [-1] * N
    dist[X] = 0
    que = [X]
    while que:
        v = que.pop(0)
        for to in edge[v]:
            if dist[to] == -1:
                dist[to] = dist[v] + 1
                que.append(to)
    #print(dist)
    ans = [0] * N
    for i in range(N):
        if dist[i] != -1:
            ans[dist[i]] += 1
    print(*ans[1:])

=======
Suggestion 6

def main():
    N,X,Y = map(int, input().split())
    #print(N,X,Y)
    G = [[] for _ in range(N+1)]
    for i in range(N-1):
        u,v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    #print(G)
    #print(G[1])
    #print(G[2])
    #print(G[3])
    #print(G[4])
    #print(G[5])
    #print(G[6])
    #print(G[7])
    #print(G[8])
    #print(G[9])
    #print(G[10])
    #print(G[11])
    #print(G[12])
    #print(G[13])
    #print(G[14])
    #print(G[15])
    #print(G[16])
    #print(G[17])
    #print(G[18])
    #print(G[19])
    #print(G[20])
    #print(G[21])
    #print(G[22])
    #print(G[23])
    #print(G[24])
    #print(G[25])
    #print(G[26])
    #print(G[27])
    #print(G[28])
    #print(G[29])
    #print(G[30])
    #print(G[31])
    #print(G[32])
    #print(G[33])
    #print(G[34])
    #print(G[35])
    #print(G[36])
    #print(G[37])
    #print(G[38])
    #print(G[39])
    #print(G[40])
    #print(G[41])
    #print(G[42])
    #print(G[43])
    #print(G[44])
    #print(G[45])
    #print(G[46])
    #print(G[47])
    #print(G[48])
    #print(G[49])
    #print(G[50])
    #print(G[51])
    #print(G[52])
    #print(G[53])
    #print(G[54])
    #print(G[55])
    #print(G[56])
    #print(G[57])
    #print(G[58])
    #print(G[59])
    #print(G[60])
    #print(G[61])

=======
Suggestion 7

def main():
    N,X,Y = map(int,input().split())
    #隣接リストを作成
    G = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u,v = map(int,input().split())
        G[u].append(v)
        G[v].append(u)
    #print(G)
    #print(G[1])
    #print(G[2])
    #print(G[3])
    #print(G[4])
    #print(G[5])
    #print(G[6])
    #print(G[7])
    #print(G[8])
    #print(G[9])
    #print(G[10])
    #print(G[11])
    #print(G[12])
    #print(G[13])
    #print(G[14])
    #print(G[15])
    #print(G[16])
    #print(G[17])
    #print(G[18])
    #print(G[19])
    #print(G[20])
    #print(G[21])
    #print(G[22])
    #print(G[23])
    #print(G[24])
    #print(G[25])
    #print(G[26])
    #print(G[27])
    #print(G[28])
    #print(G[29])
    #print(G[30])
    #print(G[31])
    #print(G[32])
    #print(G[33])
    #print(G[34])
    #print(G[35])
    #print(G[36])
    #print(G[37])
    #print(G[38])
    #print(G[39])
    #print(G[40])
    #print(G[41])
    #print(G[42])
    #print(G[43])
    #print(G[44])
    #print(G[45])
    #print(G[46])
    #print(G[47])
    #print(G[48])
    #print(G[49])
    #print(G[50])
    #print(G[51])
    #print(G[52])
    #print(G[53])
    #print(G[54])
    #print(G[55])
    #print(G[56])
    #print(G[57])
    #print(G[58])
    #print(G[59])
    #print(G[60])
    #print(G[61

=======
Suggestion 8

def main():
    N,X,Y = map(int,input().split())
    X -= 1
    Y -= 1
    #隣接リスト
    adj = [[] for _ in range(N)]
    #隣接リスト作成
    for _ in range(N-1):
        u,v = map(int,input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    #頂点 X から頂点 Y への単純パス上の頂点番号を順に空白区切りで出力せよ。
    #隣接リストを使って、BFSで探索する
    #探索は、Xからスタートして、Yに行くまでの探索である。
    #探索の経路を記録しておく。
    #探索の経路を記録するために、parentというリストを用意する。
    #parent[i]は、iの親ノードを記録する。
    #探索の経路を記録するために、parentというリストを用意する。
    #parent[i]は、iの親ノードを記録する。
    #探索の経路を記録するために、parentというリストを用意する。
    #parent[i]は、iの親ノードを記録する。
    #探索の経路を記録するために、parentというリストを用意する。
    #parent[i]は、iの親ノードを記録する。
    #探索の経路を記録するために、parentというリストを用意する。
    #parent[i]は、iの親ノードを記録する。
    #探索の経路を記録するために、parentというリストを用意する。
    #parent[i]は、iの親ノードを記録する。
    #探

=======
Suggestion 9

def main():
    #N,X,Y = map(int,input().split())
    #N,X,Y = 5,2,5
    N,X,Y = 6,1,2
    #T = [[0,0] for i in range(N-1)]
    T = [[0,0] for i in range(N-1)]
    #T = [[1,2],[1,3],[3,4],[3,5]]
    T = [[3,1],[2,5],[1,2],[4,1],[2,6]]
    #for i in range(N-1):
    #    T[i][0],T[i][1] = map(int,input().split())
    #    T[i][0] -= 1
    #    T[i][1] -= 1
    #print(T)
    #print(N,X,Y)
    #print(T)
    #print(T[0][0])
    #print(T[0][1])
    #print(T[1][0])
    #print(T[1][1])
    #print(T[2][0])
    #print(T[2][1])
    #print(T[3][0])
    #print(T[3][1])
    #print(T[4][0])
    #print(T[4][1])
    #print(T[5][0])
    #print(T[5][1])
    #print(T[6][0])
    #print(T[6][1])
    #print(T[7][0])
    #print(T[7][1])
    #print(T[8][0])
    #print(T[8][1])
    #print(T[9][0])
    #print(T[9][1])
    #print(T[10][0])
    #print(T[10][1])
    #print(T[11][0])
    #print(T[11][1])
    #print(T[12][0])
    #print(T[12][1])
    #print(T[13][0])
    #print(T[13][1])
    #print(T[14][0])
    #print(T[14][1])
    #print(T[15][0])
    #print(T[15][1])
    #print(T[16][0])
    #print(T[16][1])
    #print(T[17

=======
Suggestion 10

def main():
    # 木の頂点数
    N = int(input())
    # 木の頂点のリスト
    tree = [[] for _ in range(N+1)]
    # 木の辺のリスト
    edges = []
    # 木の頂点を受け取る
    for _ in range(N-1):
        u,v = map(int,input().split())
        tree[u].append(v)
        tree[v].append(u)
        edges.append([u,v])
    # 木の頂点のリストを辞書型に変換
    tree_dict = dict(zip(range(1,N+1),tree))
    # 木の頂点を受け取る
    X,Y = map(int,input().split())
    # 頂点Xから頂点Yへの単純パスを求める
    # 1. Xから頂点Yへのパスを求める
    path_X_Y = []
    # 1.1 Xから頂点Yへのパスを求める
    def search_path_X_Y(X,Y,path_X_Y):
        path_X_Y.append(X)
        if X == Y:
            return path_X_Y
        for node in tree_dict[X]:
            if node not in path_X_Y:
                path_X_Y = search_path_X_Y(node,Y,path_X_Y)
        return path_X_Y
    path_X_Y = search_path_X_Y(X,Y,path_X_Y)
    # 2. Xから頂点Yへの単純パスを求める
    # 2.1 Xから頂点Yへの単純パスを求める
    def search_simple_path_X_Y(path_X_Y):
        simple_path_X_Y = []
        for i in range(len(path_X_Y)-1):
            if path_X_Y[i+1] in tree_dict[path_X_Y[i]]:
                simple_path_X_Y.append(path_X_Y[i])
        simple_path_X_Y.append(path_X_Y[-1])
        return simple_path_X_Y
    simple_path_X_Y = search_simple_path_X_Y(path_X_Y)
    # 3. 頂点Xから頂点Yへの単純パ
