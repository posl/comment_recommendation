Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    C = [0] * M
    for i in range(M):
        A[i], B[i], C[i] = map(int, input().split())

    # ワーシャルフロイド
    d = [[float("inf")] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        d[i][i] = 0
    for i in range(M):
        d[A[i]][B[i]] = C[i]
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

    ans = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                if d[i][j] <= d[i][k] + d[k][j]:
                    ans += d[i][j]

    print(ans)

=======
Suggestion 2

def solve():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    C = [0] * M
    for i in range(M):
        A[i], B[i], C[i] = map(int, input().split())

    # ワーシャルフロイド法
    # 重み付きグラフの全頂点間最短路を求める
    # https://ja.wikipedia.org/wiki/%E3%83%AF%E3%83%BC%E3%82%B7%E3%83%A3%E3%83%AB%E3%83%95%E3%83%AD%E3%82%A4%E3%83%89%E6%B3%95
    # 頂点番号は 0 から始まることに注意
    INF = 10 ** 9 + 7
    d = [[INF] * N for _ in range(N)]
    for i in range(N):
        d[i][i] = 0
    for i in range(M):
        d[A[i] - 1][B[i] - 1] = C[i]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if d[i][j] == d[i][k] + d[k][j]:
                    ans += d[i][j]
                    break

    print(ans)

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))
    edges.sort(key=lambda x: x[2])
    ans = 0
    for i in range(m):
        a, b, c = edges[i]
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for j in range(i):
            a2, b2, c2 = edges[j]
            dp[a2][b2] = c2
        for k in range(1, n + 1):
            for j in range(1, n + 1):
                for l in range(1, n + 1):
                    if dp[j][k] != 0 and dp[k][l] != 0:
                        if dp[j][l] == 0:
                            dp[j][l] = dp[j][k] + dp[k][l]
                        else:
                            dp[j][l] = min(dp[j][l], dp[j][k] + dp[k][l])
        for j in range(1, n + 1):
            if dp[j][a] != 0 and dp[j][b] != 0:
                ans += dp[j][a] + dp[j][b] + c
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    G = [[float('inf')]*N for _ in range(N)]
    for _ in range(M):
        A, B, C = map(int, input().split())
        G[A-1][B-1] = C
    for i in range(N):
        G[i][i] = 0
    for k in range(N):
        for i in range(N):
            for j in range(N):
                G[i][j] = min(G[i][j], G[i][k]+G[k][j])
    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if G[i][j] > G[i][k]+G[k][j]:
                    ans += G[i][k]+G[k][j]
    print(ans)

=======
Suggestion 5

def main():
    import sys
    #入力
    readline = sys.stdin.readline
    N, M = map(int, readline().split())
    A = [0]*M
    B = [0]*M
    C = [0]*M
    for i in range(M):
        A[i], B[i], C[i] = map(int, readline().split())
        A[i] -= 1
        B[i] -= 1

    #dijkstra法
    #N:頂点数
    #M:辺の数
    #A,B:辺の始点、終点
    #C:辺のコスト
    #s:始点
    #t:終点
    #k:通っていい頂点の最大番号
    #d:始点sから各頂点への最短距離
    #d[t][k]:始点sから頂点tへの最短距離(ただし、通っていい頂点はs,t,k以下)
    def dijkstra(N, M, A, B, C, s, t, k):
        d = [[float("inf")]*N for _ in range(N)]
        d[s][s] = 0
        for i in range(N):
            for j in range(M):
                if i <= A[j] <= k and i <= B[j] <= k:
                    d[i][B[j]] = min(d[i][B[j]], d[i][A[j]]+C[j])
                    d[i][A[j]] = min(d[i][A[j]], d[i][B[j]]+C[j])
        return d[t][k]

    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                ans += dijkstra(N, M, A, B, C, i, j, k)
    print(ans)

=======
Suggestion 6

def dijkstra(s, n, d):
    INF = 10 ** 9
    dist = [INF] * n
    dist[s] = 0
    used = [False] * n
    while True:
        v = -1
        for u in range(n):
            if (not used[u]) and (v == -1):
                v = u
            elif (not used[u]) and dist[u] < dist[v]:
                v = u
        if v == -1:
            break
        used[v] = True
        for u in range(n):
            dist[u] = min(dist[u], dist[v] + d[v][u])
    return dist

n, m = map(int, input().split())
d = [[10 ** 9] * n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    d[a][b] = c
ans = 0
for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    for i in range(n):
        for j in range(n):
            if d[i][j] < 10 ** 9:
                ans += d[i][j]
print(ans)

=======
Suggestion 7

def dijkstra(s, N, graph):
    import heapq
    INF = 10**18
    dist = [INF]*N
    dist[s] = 0
    que = [(0, s)]
    while que:
        d, v = heapq.heappop(que)
        if dist[v] < d:
            continue
        for e, cost in graph[v]:
            if dist[e] > dist[v] + cost:
                dist[e] = dist[v] + cost
                heapq.heappush(que, (dist[e], e))
    return dist

=======
Suggestion 8

def dijkstra(s):
    import heapq
    d = [float("inf")] * N
    d[s] = 0
    hq = [(d[s], s)]
    while hq:
        cost, v = heapq.heappop(hq)
        if d[v] < cost:
            continue
        for nv, nc in edge[v]:
            if d[nv] > d[v] + nc:
                d[nv] = d[v] + nc
                heapq.heappush(hq, (d[nv], nv))
    return d

N, M = map(int, input().split())
edge = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    edge[a-1].append((b-1, c))
ans = 0
for i in range(N):
    d = dijkstra(i)
    for j in range(N):
        for k in range(N):
            if d[j] + d[k] <= d[i]:
                ans += d[j] + d[k]
print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(M)]
    A = [set() for _ in range(N)]
    for a, b, c in edges:
        A[a-1].add((b-1, c))
    ans = 0
    for k in range(N):
        for s in range(N):
            for t in range(N):
                if s == t:
                    continue
                dist = [float('inf')] * N
                dist[s] = 0
                for i in range(N):
                    for j in range(N):
                        if dist[j] == float('inf'):
                            continue
                        for b, c in A[j]:
                            if b > k:
                                continue
                            if dist[b] > dist[j] + c:
                                dist[b] = dist[j] + c
                if dist[t] != float('inf'):
                    ans += dist[t]
    print(ans)

=======
Suggestion 10

def dijkstra(N, G, s):
    # 1-indexed
    # N: 頂点数
    # G: 隣接リスト
    # s: 始点
    d = [float('inf')]*(N+1)
    d[s] = 0
    used = [False]*(N+1)
    used[s] = True
    edgelist = []
    for e in G[s]:
        heapq.heappush(edgelist, e)
    while len(edgelist):
        minedge = heapq.heappop(edgelist)
        if used[minedge[1]]:
            continue
        v = minedge[1]
        d[v] = minedge[0]
        used[v] = True
        for e in G[v]:
            if used[e[1]]:
                continue
            heapq.heappush(edgelist, [e[0]+d[v], e[1]])
    return d
