def main():
    N, X, Y = map(int, input().split())
    # 隣接リスト
    G = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    # 距離を格納するリスト
    dist = [-1] * (N + 1)
    # 幅優先探索
    dist[X] = 0
    q = [X]
    while q:
        v = q.pop(0)
        for nv in G[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            q.append(nv)
    # 出力
    for i in range(1, N + 1):
        if i == X:
            continue
        print(dist[i])
