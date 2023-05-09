def solve():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    # 頂点1から頂点iへの最短距離を求める
    def dijkstra(s):
        # INF = 10**10
        INF = float('inf')
        d = [INF] * N
        d[s] = 0
        used = [False] * N
        while True:
            v = -1
            for i in range(N):
                if (not used[i]) and (v == -1):
                    v = i
                elif (not used[i]) and d[i] < d[v]:
                    v = i
            if v == -1:
                break
            used[v] = True
            for i in range(N):
                d[i] = min(d[i], d[v] + T[v][i])
        return d
    # 頂点1から頂点iへの最短距離を求める
    d = dijkstra(0)
    # 頂点iから頂点jへの最短距離がKとなる経路を求める
    ans = 0
    for i in range(N):
        for j in range(N):
            if d[i] + T[i][j] + d[j] == K:
                ans += 1
    print(ans // 2)
