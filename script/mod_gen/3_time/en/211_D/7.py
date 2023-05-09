def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    # 1から各頂点への最短距離を求める
    # 隣接行列を作成
    adj = [[0] * N for _ in range(N)]
    for a, b in AB:
        adj[a - 1][b - 1] = 1
        adj[b - 1][a - 1] = 1
    # ダイクストラ法
    d = [float("inf")] * N
    d[0] = 0
    q = [0]
    while q:
        u = q.pop(0)
        for v in range(N):
            if adj[u][v] == 1 and d[v] > d[u] + 1:
                d[v] = d[u] + 1
                q.append(v)
    # 最短距離がN-1の頂点数を求める
    print(d.count(N - 1))

if __name__ == '__main__':
    main()