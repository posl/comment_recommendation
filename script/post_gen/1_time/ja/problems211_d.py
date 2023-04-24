Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    road = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        road[a].append(b)
        road[b].append(a)
    ans = 0
    for i in range(len(road[1])):
        if N in road[road[1][i]]:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    import sys
    input = sys.stdin.readline
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        A -= 1
        B -= 1
        G[A].append(B)
        G[B].append(A)

    # BFS
    from collections import deque
    dist = [-1] * N
    dist[0] = 0
    que = deque([0])
    while que:
        v = que.popleft()
        for nv in G[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            que.append(nv)

    if dist[N-1] == -1:
        print(0)
        return

    # 最短経路の数を数える
    ans = 0
    que = deque([N-1])
    while que:
        v = que.popleft()
        for nv in G[v]:
            if dist[nv] != dist[v] - 1:
                continue
            ans += 1
            que.append(nv)

    print(ans % (10**9+7))

=======
Suggestion 3

def main():
    #入力
    N, M = map(int, input().split())
    edge = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        edge[a-1].append(b-1)
        edge[b-1].append(a-1)
    #print(edge)
    #BFS
    q = [0]
    distance = [-1] * N
    distance[0] = 0
    cnt = [0] * N
    cnt[0] = 1
    while q:
        v = q.pop(0)
        for nv in edge[v]:
            if distance[nv] == -1:
                distance[nv] = distance[v] + 1
                q.append(nv)
                cnt[nv] = cnt[v]
            elif distance[nv] == distance[v] + 1:
                cnt[nv] = (cnt[nv] + cnt[v]) % (10**9+7)
    #print(distance)
    #print(cnt)
    #出力
    print(cnt[N-1])

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    G = [[] for _ in range(N+1)]
    for a, b in AB:
        G[a].append(b)
        G[b].append(a)
    MOD = 10**9 + 7
    INF = 10**18
    dist = [INF] * (N+1)
    cnt = [0] * (N+1)
    dist[1] = 0
    cnt[1] = 1
    Q = [1]
    while Q:
        v = Q.pop()
        for nv in G[v]:
            if dist[nv] == INF:
                dist[nv] = dist[v] + 1
                cnt[nv] = cnt[v]
                Q.append(nv)
            elif dist[nv] == dist[v] + 1:
                cnt[nv] += cnt[v]
                cnt[nv] %= MOD
    print(cnt[N])

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    if M == 0:
        print(0)
        return
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB = sorted(AB, key=lambda x: x[1])
    #print(AB)
    cnt = 1
    prev = AB[0][1]
    for i in range(1, M):
        if AB[i][0] < prev:
            continue
        cnt += 1
        prev = AB[i][1]
    print(cnt)

=======
Suggestion 6

def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    mod = 10**9+7
    N,M = map(int,input().split())
    if M == 0:
        print(0)
        return
    G = [[] for _ in range(N+1)]
    for _ in range(M):
        a,b = map(int,input().split())
        G[a].append(b)
        G[b].append(a)
    dist = [-1]*(N+1)
    dist[1] = 0
    q = deque()
    q.append(1)
    path = [0]*(N+1)
    path[1] = 1
    while q:
        now = q.popleft()
        for nex in G[now]:
            if dist[nex] == -1:
                dist[nex] = dist[now] + 1
                path[nex] = path[now]
                q.append(nex)
            elif dist[nex] == dist[now] + 1:
                path[nex] += path[now]
                path[nex] %= mod
    print(path[N])

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    MOD = 10 ** 9 + 7
    path = [[] for _ in range(N)]
    for a, b in AB:
        path[a - 1].append(b - 1)
        path[b - 1].append(a - 1)
    # print(path)
    dp = [0] * N
    dp[0] = 1
    for i in range(N):
        for j in path[i]:
            dp[j] += dp[i]
            dp[j] %= MOD
    print(dp[N - 1])

=======
Suggestion 8

def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 9)
    
    MOD = 10**9+7
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    # 隣接リスト
    G = [[] for _ in range(N+1)]
    for a, b in AB:
        G[a].append(b)
        G[b].append(a)
    # 1 から N への最短距離
    dist = [0] * (N+1)
    dist[1] = 1
    # 1 から N への経路数
    path = [0] * (N+1)
    path[1] = 1
    # 1 から N への経路
    route = [[] for _ in range(N+1)]
    route[1] = [1]
    # 1 から N への経路を探索
    que = deque([1])
    while que:
        v = que.popleft()
        for nv in G[v]:
            if dist[nv] == 0:
                dist[nv] = dist[v] + 1
                path[nv] = path[v]
                route[nv] = route[v] + [nv]
                que.append(nv)
            elif dist[nv] == dist[v] + 1:
                path[nv] += path[v]
                path[nv] %= MOD
    print(path[N])

=======
Suggestion 9

def main():
    #N: 都市数, M: 道路数
    N, M = map(int, input().split())
    #都市1から各都市への道路の数
    road = [0] * (N + 1)
    #都市1から各都市への道路数をカウント
    for i in range(M):
        A, B = map(int, input().split())
        road[A] += 1
        road[B] += 1
    #都市1から各都市への道路数が0のものは都市1から都市Nへ移動できないので0を出力
    if road[1] == 0 or road[N] == 0:
        print(0)
    else:
        #都市1から都市Nへの道路数を出力
        print(road[1] * road[N])

=======
Suggestion 10

def dfs(G, s):
    # s: start node
    # G: adjacency list
    # R: return value
    # V: visited
    # P: previous
    # D: distance
    # L: layer
    R = {}
    V = [False] * len(G)
    P = [-1] * len(G)
    D = [0] * len(G)
    L = [0] * len(G)
    def dfs_visit(G, u):
        V[u] = True
        for v in G[u]:
            if not V[v]:
                P[v] = u
                D[v] = D[u] + 1
                L[v] = L[u] + 1
                dfs_visit(G, v)
    dfs_visit(G, s)
    R['V'] = V
    R['P'] = P
    R['D'] = D
    R['L'] = L
    return R
