def main():
    # 標準入力の受け取り
    N, M = map(int, input().split())
    # グラフの初期化
    G = [[] for i in range(N)]
    # グラフの辺の受け取り
    for i in range(M):
        u, v = map(int, input().split())
        G[u - 1].append(v - 1)
        G[v - 1].append(u - 1)
    # 頂点0から各頂点への最短距離を求める
    dist = [-1] * N
    dist[0] = 0
    q = [0]
    while q:
        x = q.pop(0)
        for y in G[x]:
            if dist[y] == -1:
                dist[y] = dist[x] + 1
                q.append(y)
    # 頂点0から各頂点への最短距離が3の倍数の頂点の個数を求める
    cnt = 0
    for i in range(N):
        if dist[i] % 3 == 0:
            cnt += 1
    # 頂点0から各頂点への最短距離が3の倍数の頂点の個数から、
    # 頂点0から最短距離が3の倍数の頂点への辺の本数を引いたものが、
    # 求める答え
    ans = cnt * (cnt - 1) // 2 - M
    # 答えの出力
    print(ans)

if __name__ == '__main__':
    main()