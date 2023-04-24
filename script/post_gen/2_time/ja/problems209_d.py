Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N-1)]
    CD = [list(map(int, input().split())) for _ in range(Q)]

    # 隣接リストの作成
    adj = [[] for _ in range(N+1)]
    for a, b in AB:
        adj[a].append(b)
        adj[b].append(a)

    # 頂点 1 を根とする木の構築
    parent = [0] * (N+1)
    parent[1] = -1
    stack = [1]
    while stack:
        v = stack.pop()
        for w in adj[v]:
            if parent[w] == 0:
                parent[w] = v
                stack.append(w)

    # 頂点 v から根への距離を求める
    depth = [0] * (N+1)
    for v in range(1, N+1):
        d = 0
        w = v
        while parent[w] != -1:
            d += 1
            w = parent[w]
        depth[v] = d

    # クエリの処理
    for c, d in CD:
        if depth[c] % 2 == depth[d] % 2:
            print('Town')
        else:
            print('Road')

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N - 1)]
    CD = [list(map(int, input().split())) for _ in range(Q)]
    graph = [[] for _ in range(N + 1)]
    for a, b in AB:
        graph[a].append(b)
        graph[b].append(a)
    #print(graph)
    #print(CD)
    # 頂点1からの最短距離を求める
    # 始点を1とする
    s = 1
    # 各頂点の最短距離を格納する配列
    dist = [-1] * (N + 1)
    # 始点の距離を0とする
    dist[s] = 0
    # BFS用のキューを用意
    que = [s]
    # BFS開始
    while que:
        # キューから頂点を取り出す
        v = que.pop(0)
        # 頂点vから辿れる頂点を全て調べる
        for nv in graph[v]:
            # すでに最短距離が求まっているならスルー
            if dist[nv] != -1:
                continue
            # 新たな頂点なので距離を記録してキューに入れる
            dist[nv] = dist[v] + 1
            que.append(nv)
    #print(dist)
    for c, d in CD:
        if (dist[c] + dist[d]) % 2 == 0:
            print('Town')
        else:
            print('Road')

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)
    depth = [-1] * N
    depth[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for nv in G[v]:
            if depth[nv] == -1:
                depth[nv] = depth[v] + 1
                stack.append(nv)
    for _ in range(Q):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        if (depth[c] + depth[d]) % 2 == 0:
            print("Town")
        else:
            print("Road")

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    edge = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        a, b = a-1, b-1
        edge[a].append(b)
        edge[b].append(a)
    depth = [-1] * N
    depth[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for u in edge[v]:
            if depth[u] != -1:
                continue
            depth[u] = depth[v] + 1
            stack.append(u)
    for _ in range(Q):
        c, d = map(int, input().split())
        c, d = c-1, d-1
        if (depth[c] + depth[d]) % 2 == 0:
            print("Town")
        else:
            print("Road")

=======
Suggestion 5

def main():
    import sys
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N-1)]
    CD = [list(map(int, input().split())) for _ in range(Q)]

    # 隣接リストを作る
    adj = [[] for _ in range(N+1)]
    for a, b in AB:
        adj[a].append(b)
        adj[b].append(a)

    # BFS
    from collections import deque
    q = deque()
    q.append(1)
    dist = [-1] * (N+1)
    dist[1] = 0
    while q:
        v = q.popleft()
        for nv in adj[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                q.append(nv)

    for c, d in CD:
        if (dist[c] + dist[d]) % 2 == 0:
            print('Town')
        else:
            print('Road')

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    # 隣接リスト
    adj = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
    # クエリ
    query = [list(map(int, input().split())) for _ in range(Q)]
    # 各クエリについて
    for c, d in query:
        c -= 1
        d -= 1
        # 高橋君の距離
        dist_c = [-1] * N
        dist_c[c] = 0
        # 青木君の距離
        dist_d = [-1] * N
        dist_d[d] = 0
        # 高橋君の探索
        stack = [c]
        while stack:
            v = stack.pop()
            for u in adj[v]:
                if dist_c[u] != -1:
                    continue
                dist_c[u] = dist_c[v] + 1
                stack.append(u)
        # 青木君の探索
        stack = [d]
        while stack:
            v = stack.pop()
            for u in adj[v]:
                if dist_d[u] != -1:
                    continue
                dist_d[u] = dist_d[v] + 1
                stack.append(u)
        # 出力
        if dist_c[d] % 2 == dist_d[c] % 2:
            print("Town")
        else:
            print("Road")

=======
Suggestion 7

def init():
    global N, Q, a, b, c, d
    N, Q = map(int, input().split())
    a = [0] * (N-1)
    b = [0] * (N-1)
    for i in range(N-1):
        a[i], b[i] = map(int, input().split())
    c = [0] * Q
    d = [0] * Q
    for i in range(Q):
        c[i], d[i] = map(int, input().split())

=======
Suggestion 8

def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    
    N,Q = map(int,input().split())
    edge = [[] for i in range(N+1)]
    for i in range(N-1):
        a,b = map(int,input().split())
        edge[a].append(b)
        edge[b].append(a)
    
    depth = [-1]*(N+1)
    depth[1] = 0
    que = deque([1])
    while que:
        p = que.popleft()
        for i in edge[p]:
            if depth[i] == -1:
                depth[i] = depth[p]+1
                que.append(i)
    
    for i in range(Q):
        c,d = map(int,input().split())
        if abs(depth[c]-depth[d])%2 == 0:
            print("Town")
        else:
            print("Road")

=======
Suggestion 9

def main():
    N,Q=map(int,input().split())
    #print(N,Q)
    #N=4
    #Q=1
    #a=[1,2,2,4]
    #b=[2,3,4,1]
    #c=[1,2]
    #d=[2,1]
    a=[]
    b=[]
    c=[]
    d=[]
    for i in range(N-1):
        x,y=map(int,input().split())
        a.append(x)
        b.append(y)
    for i in range(Q):
        x,y=map(int,input().split())
        c.append(x)
        d.append(y)
    #print(a,b,c,d)
    #print(a,b)
    #print(c,d)
    #pri

=======
Suggestion 10

def input(): return sys.stdin.readline().strip()
