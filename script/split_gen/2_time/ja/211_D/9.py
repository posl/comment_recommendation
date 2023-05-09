def solve(N, M, AB):
    import sys
    sys.setrecursionlimit(10**6)
    mod = 10**9+7
    # 入力
    # 隣接リスト
    G = [[] for _ in range(N)]
    for a, b in AB:
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    # 探索
    # 1からNへの最短経路の個数
    # BFS
    from collections import deque
    # キュー
    queue = deque()
    queue.append(0)
    # 訪問済み
    visited = [False]*N
    visited[0] = True
    # 遷移元
    prev = [-1]*N
    # 遷移元からの距離
    dist = [-1]*N
    dist[0] = 0
    # BFS
    while queue:
        # キューから取り出す
        now = queue.popleft()
        # 隣接リストを調べる
        for next in G[now]:
            if visited[next]:
                continue
            # 訪問済みにする
            visited[next] = True
            # キューに入れる
            queue.append(next)
            # 遷移元を記録
            prev[next] = now
            # 遷移元からの距離を記録
            dist[next] = dist[now]+1
    # 出力
    if dist[N-1] == -1:
        print(0)
    else:
        # 1からNへの最短経路
        path = []
        now = N-1
        while now != -1:
            path.append(now)
            now = prev[now]
        path.reverse()
        # 1からNへの最短経路の個数
        # 各都市の遷移元の数
        num = [0]*N
        num[0] = 1
        for i in range(1, N):
            num[i] = 1
