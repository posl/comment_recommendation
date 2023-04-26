Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)
    dist = [None] * N
    dist[0] = 0
    q = [0]
    while q:
        v = q.pop()
        for nv in G[v]:
            if dist[nv] is None:
                dist[nv] = dist[v] + 1
                q.append(nv)
    if dist[-1] is None:
        print(0)
        return
    cnt = 0
    for v in G[-1]:
        if dist[v] == dist[-1] - 1:
            cnt += 1
    print(cnt)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    dist = [-1] * N
    dist[0] = 0
    q = [0]
    while q:
        v = q.pop()
        for nv in graph[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                q.append(nv)
    if dist[-1] == -1:
        print(0)
    else:
        print(dist.count(dist[-1]))

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    if M == 0:
        print(0)
        return
    edge = [[] for i in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        edge[a - 1].append(b - 1)
        edge[b - 1].append(a - 1)
    dist = [-1] * N
    dist[0] = 0
    q = [0]
    while q:
        v = q.pop()
        for nv in edge[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            q.append(nv)
    if dist[N - 1] == -1:
        print(0)
        return
    ans = 0
    for i in range(N):
        if dist[i] == dist[N - 1] - 1:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    if M == 0:
        print(0)
        return
    if N == 2:
        print(1)
        return
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    dist = [-1]*N
    dist[0] = 0
    q = [0]
    while len(q) > 0:
        v = q.pop(0)
        for nv in G[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            q.append(nv)
    if dist[-1] == -1:
        print(0)
        return
    ans = 1
    for d in dist:
        if d == 2:
            ans *= len(G[d])
    print(ans%(10**9+7))

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    if M == 0:
        print(0)
        return
    # 隣接リスト
    adj = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
    # 隣接リストを隣接行列に変換
    # adj_mat = [[0] * N for _ in range(N)]
    # for i in range(N):
    #     for j in adj[i]:
    #         adj_mat[i][j] = 1
    #         adj_mat[j][i] = 1
    # print(adj_mat)
    # 始点
    start = 0
    # 終点
    goal = N-1
    # 経路数
    paths = 0
    # 深さ優先探索
    stack = [start]
    while stack:
        cur = stack.pop()
        if cur == goal:
            paths += 1
            continue
        for i in adj[cur]:
            if i in stack:
                continue
            stack.append(i)
    print(paths % (10**9+7))

=======
Suggestion 6

def main():
    n,m = map(int,input().split())
    if m == 0:
        print(0)
        return
    # 隣接リスト
    adj = [[] for _ in range(n)]
    for _ in range(m):
        a,b = map(int,input().split())
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
    # 1からNへの最短経路
    dist = [float('inf')]*n
    dist[0] = 0
    # 1からNへの最短経路の数
    count = [0]*n
    count[0] = 1
    # 幅優先探索
    q = [0]
    while q:
        v = q.pop(0)
        d = dist[v]
        for nv in adj[v]:
            if dist[nv] > d+1:
                dist[nv] = d+1
                count[nv] = count[v]
                q.append(nv)
            elif dist[nv] == d+1:
                count[nv] += count[v]
                count[nv] %= 10**9+7
    print(count[-1])

=======
Suggestion 7

def main():
    #入力
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(M)]
    #print("N = ", N)
    #print("M = ", M)
    #print("AB = ", AB)

    #都市 1 から都市 N へ移動することが出来ない場合は 0 と出力せよ。
    if N == 1:
        print(0)
        return

    #都市 1 から都市 N へ最も早く移動することができる経路は何通りありますか？
    #都市 1 から都市 N へ移動することが出来ない場合は 0 と出力せよ。
    #都市 1 から都市 N へは最短 2 時間で移動することができ、それを実現する経路は 1 -> 2 -> 4 と 1 -> 3 -> 4 の 2 つです。
    #都市 1 から都市 N へは最短 3 時間で移動することができ、それを実現する経路は 1 -> 3 -> 2 -> 4 の 1 つです。
    #都市 1 から都市 N  に移動することはできません。この場合 0 を出力してください。
    #都市 1 から都市 N へは最短 4 時間で移動することができ、それを実現する経路は 1 -> 3 -> 2 -> 4 の 1 つです。

    #都市 1 から都市 N へ移動することが出来ない場合は 0 と出力せよ。
    #都市 1 から都市 N  に移動することはできません。この場合 0 を出力してください。
    #都市

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    if M == 0:
        print(0)
        return
    MOD = 10**9+7
    # 隣接リスト
    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    # 隣接リストの各都市の隣接都市の数を数える
    # つまり、隣接都市の数が1の都市は、都市1から都市Nへの経路において、
    # 隣接都市の数が2以上の都市を通る必要がある
    # そのため、隣接都市の数が1の都市を数える
    one_adj = [0] * (N+1)
    for i in range(1, N+1):
        one_adj[i] = len(adj[i]) == 1
    # 都市1から都市Nへの経路の数を数える
    # つまり、隣接都市の数が1の都市を通る経路の数を数える
    # 都市1から都市Nへの経路の数は、都市1から都市Nへの経路の数を数える
    # 都市1から都市Nへの経路の数は、都市1から都市Nへの経路の数を数える
    # 都市1から都市Nへの経路の数は、都市1から都市Nへの経路の数を数える
    # 都市1から都市Nへの経路の数は、都市1から都市Nへの経路の数を数える
    # 都市1から都市Nへの経路の数は、都市1から都市Nへの経路の数を数え

=======
Suggestion 9

def main():
    #入力
    N, M = map(int, input().split())
    #都市の数はN個なので、N+1個のリストを用意する
    #都市の数だけリストを用意して、都市の番号に対応するリストの中に、
    #その都市に接続している都市の番号を格納する
    #都市の番号は1から始まるので、リストの要素番号をそのまま都市の番号とするために、
    #都市の数+1個のリストを用意する
    city = [[] for i in range(N+1)]
    for i in range(M):
        A, B = map(int, input().split())
        city[A].append(B)
        city[B].append(A)
    #print(city)

    #都市の数はN個なので、N+1個のリストを用意する
    #都市の数だけリストを用意して、都市の番号に対応するリストの中に、
    #その都市に接続している都市の番号を格納する
    #都市の番号は1から始まるので、リストの要素番号をそのまま都市の番号とするために、
    #都市の数+1個のリストを用意する
    #都市の数はN個なので、N+1個のリストを用意する
    #都市の数だけリストを用意して、都市の番号に対応するリストの中に、
    #その都市に接続している都市の番号を格納する
    #都市の番号は1から始まるので、リストの要素番号をそのまま都市の番号とするために、
    #都市の数+1個のリストを用意する
    city = [[] for i in range(N+1
