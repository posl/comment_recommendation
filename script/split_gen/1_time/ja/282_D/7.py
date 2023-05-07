def solve():
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    # 頂点の接続関係を記録
    graph = [[] for _ in range(N+1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    # 頂点の色を記録
    color = [0] * (N+1)
    # 二部グラフか判定
    def dfs(v, c):
        color[v] = c
        for nv in graph[v]:
            if color[nv] == c:
                return False
            if color[nv] == 0 and not dfs(nv, -c):
                return False
        return True
    ans = 0
    for i in range(1, N+1):
        if color[i] == 0:
            if dfs(i, 1):
                ans += 1
    print(ans)
