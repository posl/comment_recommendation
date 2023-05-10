def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    # 隣接リスト
    adj = [[] for _ in range(n)]
    for a, b in ab:
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
    # 頂点 0 から各頂点への最短距離
    dist = [-1] * n
    dist[0] = 0
    # 頂点 0 から各頂点への最短経路数
    cnt = [0] * n
    cnt[0] = 1
    # 幅優先探索
    from collections import deque
    q = deque()
    q.append(0)
    while q:
        v = q.popleft()
        for nv in adj[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            cnt[nv] = cnt[v]
            q.append(nv)
        # 頂点 0 から頂点 n-1 への最短経路が求まったら探索を終了
        if dist[n-1] != -1:
            break
    print(cnt[n-1] % (10**9+7))
