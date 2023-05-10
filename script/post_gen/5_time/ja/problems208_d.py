Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N,M = map(int,input().split())
    #A = []
    #B = []
    #C = []
    #for i in range(M):
    #    a,b,c = map(int,input().split())
    #    A.

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    INF = 10**9
    # dp[i][j]は都市iから都市jへの最短距離
    dp = [[INF for i in range(N+1)] for j in range(N+1)]
    # 道路の情報をdpに格納
    for i in range(M):
        A, B, C = map(int, input().split())
        dp[A][B] = C

    # dpの初期化
    for i in range(N+1):
        dp[i][i] = 0

    # dpの更新
    # dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])

    # 答えの計算
    ans = 0
    for s in range(1, N+1):
        for t in range(1, N+1):
            for k in range(1, N+1):
                if s == t or s == k or t == k:
                    continue
                ans += dp[s][t]
    print(ans)

=======
Suggestion 3

def solve():
    pass

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        A, B, C = map(int, input().split())
        edges.append((A, B, C))
    edges.sort(key=lambda x: x[2])

    # ワーシャルフロイド法
    # dp[i][j][k] := iからjにk以下の都市を通って行く最短経路
    INF = 10**10
    dp = [[[INF for _ in range(N+1)] for _ in range(N+1)] for _ in range(N+1)]
    for i in range(N+1):
        for j in range(N+1):
            if i == j:
                dp[i][j][i] = 0
    for i in range(N+1):
        for j in range(N+1):
            for k in range(N+1):
                dp[i][j][k] = min(dp[i][j][k], dp[i][j][k])
                dp[i][j][k] = min(dp[i][j][k], dp[i][j][k])

    for i in range(N+1):
        for j in range(N+1):
            for k in range(N+1):
                dp[i][j][k] = min(dp[i][j][k], dp[i][j][k])
                dp[i][j][k] = min(dp[i][j][k], dp[i][j][k])

    for i in range(N+1):
        for j in range(N+1):
            for k in range(N+1):
                dp[i][j][k] = min(dp[i][j][k], dp[i][j][k])
                dp[i][j][k] = min(dp[i][j][k], dp[i][j][k])

    for i in range(N+1):
        for j in range(N+1):
            for k in range(N+1):
                dp[i][j][k] = min(dp[i][j][k], dp[i][j][k])
                dp[i][j][k] = min(dp[i][j][k], dp[i][j][k])

    for i in range(N+1):
        for j in range(N+1):
            for k

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    G = [[float('inf')]*N for _ in range(N)]
    for i in range(N):
        G[i][i] = 0
    for _ in range(M):
        a, b, c = map(int, input().split())
        G[a-1][b-1] = c
    for k in range(N):
        for i in range(N):
            for j in range(N):
                G[i][j] = min(G[i][j], G[i][k]+G[k][j])
    ans = 0
    for s in range(N):
        for t in range(N):
            for k in range(N):
                if s == t or s == k or t == k:
                    continue
                if G[s][t] == G[s][k]+G[k][t]:
                    ans += G[s][t]
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    ABC = [list(map(int, input().split())) for _ in range(M)]
    INF = 10**18
    cost = [[INF for _ in range(N + 1)] for _ in range(N + 1)]
    for i in range(1, N + 1):
        cost[i][i] = 0
    for A, B, C in ABC:
        cost[A][B] = C
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
    ans = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                if i == j or j == k or k == i:
                    continue
                ans += cost[i][j] + cost[j][k] + cost[k][i]
    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    ABC = [list(map(int, input().split())) for _ in range(M)]
    INF = 10 ** 9
    D = [[INF] * N for _ in range(N)]
    for i in range(N):
        D[i][i] = 0
    for a, b, c in ABC:
        D[a - 1][b - 1] = c
    for k in range(N):
        for i in range(N):
            for j in range(N):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    ans = 0
    for s in range(N):
        for t in range(N):
            for k in range(N):
                if D[s][t] == D[s][k] + D[k][t]:
                    ans += D[s][t]
                    break
    print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    C = []
    for i in range(M):
        a, b, c = map(int, input().split())
        A.append(a-1)
        B.append(b-1)
        C.append(c)

    ans = 0
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                if i > k or j > k:
                    continue
                ans += min(C[i]+C[j], C[k])

    print(ans)

=======
Suggestion 9

def dijkstra(s, N, G):
    color = [0] * N
    d = [float('inf')] * N
    d[s] = 0
    color[s] = 1
    while(1):
        minv = float('inf')
        for i in range(N):
            if color[i] != 2 and d[i] < minv:
                minv = d[i]
                u = i
        if minv == float('inf'):
            break
        color[u] = 2
        for v in range(N):
            if color[v] != 2 and G[u][v] != float('inf'):
                if d[u] + G[u][v] < d[v]:
                    d[v] = d[u] + G[u][v]
                    color[v] = 1
    return d

N,M = map(int,input().split())
G = [[float('inf') for i in range(N)] for j in range(N)]
for i in range(M):
    A,B,C = map(int,input().split())
    G[A-1][B-1] = C

ans = 0
for i in range(N):
    d = dijkstra(i,N,G)
    for j in range(N):
        for k in range(N):
            if d[j] + G[j][k] == d[k]:
                ans += d[j]
print(ans)

=======
Suggestion 10

def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    n = len(d)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k]+d[k][j])
    return d
