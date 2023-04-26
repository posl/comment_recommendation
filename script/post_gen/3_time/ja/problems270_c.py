Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    tree = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        tree[u].append(v)
        tree[v].append(u)
    
    ans = [0] * N
    for i in range(N):
        if i == X:
            continue
        dist = [-1] * N
        dist[i] = 0
        q = [i]
        while q:
            v = q.pop()
            for w in tree[v]:
                if dist[w] == -1:
                    dist[w] = dist[v] + 1
                    q.append(w)
        ans[i] = dist[Y]
    
    for i in range(N):
        if i == X:
            continue
        print(i+1, ans[i])

=======
Suggestion 2

def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    edge = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edge[u].append(v)
        edge[v].append(u)

    dist = [-1] * N
    dist[X] = 0
    q = [X]
    while q:
        x = q.pop()
        for y in edge[x]:
            if dist[y] == -1:
                dist[y] = dist[x] + 1
                q.append(y)

    ans = [0] * N
    for i, d in enumerate(dist):
        ans[d] += 1
    for i in range(1, N):
        print(ans[i] // 2)

=======
Suggestion 3

def main():
    N,X,Y = map(int,input().split())
    edge = [[] for i in range(N+1)]
    for i in range(N-1):
        u,v = map(int,input().split())
        edge[u].append(v)
        edge[v].append(u)
    #print(edge)
    #print("X=",X,"Y=",Y)
    #print("N=",N)
    #print("N-1=",N-1)
    #print("edge=",edge)
    #print(len(edge))
    #print(len(edge[1]))
    #print(len(edge[2]))
    #print(len(edge[3]))
    #print(len(edge[4]))
    #print(len(edge[5]))
    #print(len(edge[6]))
    #print("edge[1]=",edge[1])
    #print("edge[2]=",edge[2])
    #print("edge[3]=",edge[3])
    #print("edge[4]=",edge[4])
    #print("edge[5]=",edge[5])
    #print("edge[6]=",edge[6])
    #print("edge[1][0]=",edge[1][0])
    #print("edge[1][1]=",edge[1][1])
    #print("edge[1][2]=",edge[1][2])
    #print("edge[2][0]=",edge[2][0])
    #print("edge[2][1]=",edge[2][1])
    #print("edge[3][0]=",edge[3][0])
    #print("edge[3][1]=",edge[3][1])
    #print("edge[4][0]=",edge[4][0])
    #print("edge[5][0]=",edge[5][0])
    #print("edge[6][0]=",edge[6][0])
    #print("edge[1][0]=",edge[1][0])
    #print("edge[1][1]=",edge[1][1])
    #print("edge[1][2]=",edge[1][2])
    #print("edge[2][0]=",edge[2][0])
    #print("edge[2][1]=",edge[2][1])
    #print("edge[3][0]

=======
Suggestion 4

def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    tree = [[] for _ in range(N)]
    for i in range(N-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        tree[u].append(v)
        tree[v].append(u)
    dist = [-1] * N
    dist[X] = 0
    que = [X]
    while que:
        x = que.pop()
        for y in tree[x]:
            if dist[y] == -1:
                dist[y] = dist[x] + 1
                que.append(y)
    for i in range(N):
        if dist[i] == -1:
            dist[i] = dist[Y] + 1
            que.append(i)
    while que:
        x = que.pop()
        for y in tree[x]:
            if dist[y] == -1:
                dist[y] = dist[x] + 1
                que.append(y)
    ans = [0] * (N-1)
    for i in range(N):
        if i != X:
            ans[dist[i]-1] += 1
    print(*ans)

=======
Suggestion 5

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

    # 幅優先探索
    # 頂点 X から頂点 Y への単純パス上の頂点を順に列挙して返す
    def bfs(X, Y):
        # X から Y への単純パス上の頂点を順に列挙する
        # ただし、X から Y への単純パスが存在しない場合は None を返す
        # 頂点 X から頂点 Y への単純パス上の頂点を順に列挙する
        # ただし、X から Y への単純パスが存在しない場合は None を返す
        # 幅優先探索で X から Y への単純パス上の頂点を順に列挙する
        # 頂点 X から頂点 Y への単純パスが存在しない場合は None を返す
        # 頂点 X から頂点 Y への単純パスが存在する場合は、
        # 頂点 X から頂点 Y への単純パス上の頂点を順に列挙したリストを返す
        # 幅優先探索
        # 頂点 X から頂点 Y への単純パス上の頂点を順に列挙して返す
        # 頂点 X から

=======
Suggestion 6

def main():
    N, X, Y = map(int, input().split())
    # 隣接リストを作成
    graph = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # 頂点 X から頂点 Y への単純パスを求める
    # 単純パスとは、頂点列 v_1,v_2, ..., v_k であって、
    # v_1=X, v_k=Y かつ、1≦ i≦ k-1 に対して v_i と v_{i+1} が辺で結ばれているようなものを頂点 X から頂点 Y へのパス と呼びます。
    # さらに、v_1,v_2, ..., v_k がすべて異なるようなものを頂点 X から頂点 Y への 単純パス と呼びます。
    # 木 T 上の任意の相異なる 2 頂点 a,b について、a から b への単純パスがただ一つ存在することが証明できます。
    # 木 T の頂点 X から頂点 Y への単純パスを求めるには、以下の手順で求めます。
    # 1. 頂点 X から頂点 Y への距離を求める
    # 2. 頂点 Y から頂点 X への距離を求める
    # 3. 1. と 2. で求めた距離を比較する
    # 4. 1. と 2. で求めた距離が等しい場合、頂点 X

=======
Suggestion 7

def main():
    #入力
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1

    #隣接リスト
    adj = [[] for _ in range(N)]

    for _ in range(N-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        adj[a].append(b)
        adj[b].append(a)

    #Xからの距離
    dist = [-1]*N
    dist[X] = 0
    #Xからの距離が最も遠い頂点
    farthest = X

    #BFS
    que = [X]
    while que:
        v = que.pop()
        for nv in adj[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            que.append(nv)
            #Xからの距離が最も遠い頂点を更新
            if dist[nv] > dist[farthest]:
                farthest = nv

    #Yからの距離
    dist = [-1]*N
    dist[Y] = 0

    #BFS
    que = [Y]
    while que:
        v = que.pop()
        for nv in adj[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            que.append(nv)

    #Xからの距離が最も遠い頂点からYへの距離が最も遠い頂点までの距離を求める
    ans = 0
    for i in range(N):
        if i == farthest:
            continue
        if dist[i] > dist[farthest]:
            ans = max(ans, dist[i])

    print(ans)

=======
Suggestion 8

def main():
    N, X, Y = map(int, input().split())
    # 頂点番号を 0 から N-1 に変換する
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
    # X から Y への単純パスを列挙する
    # まず、X から Y へのパスを列挙する
    # この時、隣接する頂点のうち、X よりも Y に近い方を選ぶ
    # この時、X から Y へのパスは必ず単純パスになる
    # 例えば、X から Y へのパスが X -> a -> b -> Y となっているとする
    # この時、a よりも Y に近い方の頂点を選ぶと、X -> b -> Y となる
    # この時、X -> Y のパスが存在するので、X -> b -> Y は単純パスにならない
    # したがって、X から Y へのパスは必ず単純パスになる
    # また、X よりも Y に近い方の頂点は、X から Y へのパス上に存在する
    # したがって、X から Y へのパスは単純パスになる
    # したがって、X から Y への単純パスは、X から Y へのパスになる
    # つまり、X から Y へのパスのうち、X よりも Y に近い

=======
Suggestion 9

def main():
    N, X, Y = map(int, input().split())
    edges = []
    for _ in range(N - 1):
        edges.append(list(map(int, input().split())))
    print(edges)
    # print(N, X, Y)
    # print(edges)
    # return
    # 木の構造を作る
    # 隣接リストで表現する
    # 木の構造を作る
    # 隣接リストで表現する
    tree = [[] for _ in range(N + 1)]
    for e in edges:
        tree[e[0]].append(e[1])
        tree[e[1]].append(e[0])
    print(tree)
    # return
    # 頂点Xから頂点Yへの単純パスを求める
    # 頂点Xから頂点Yへの単純パスを求める
    # BFSで探索する
    # 頂点Xからの距離を求める
    # 頂点Yからの距離を求める
    # 頂点Xから頂点Yへの単純パスを求める
    # 頂点Xから頂点Yへの単純パスを求める
    # BFSで探索する
    # 頂点Xからの距離を求める
    # 頂点Yからの距離を求める
    # 頂点Xから頂点Yへの単純パスを求める
    # 頂点Xから頂点Yへの単純パスを求める
    # BFSで探索する
    # 頂点Xからの距離を求める
    # 頂点Yからの距離を求める
    # 頂点Xから頂点Yへの単純パスを求める
    # 頂点Xから頂点Yへの単

=======
Suggestion 10

def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    #グラフを生成
    graph = [ [] for _ in range(N) ]
    for i in range(N-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    #XからYへの単純パスを列挙
    path = []
    path = dfs(graph, X, Y, path)
    #pathを出力
    for i in range(len(path)):
        if i == 0:
            print(path[i]+1, end="")
        else:
            print(" ", path[i]+1, sep="", end="")
    print()
