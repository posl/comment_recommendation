def main():
    n, m = map(int, input().split())
    if n == 2:
        print(0)
        exit()
    if m == 0:
        print(0)
        exit()
    # 都市間の道路をリストで表現
    road = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        road[a-1].append(b-1)
        road[b-1].append(a-1)
    # 1から各都市への最短経路数をリストで表現
    # 1からの距離を表す
    dist = [0 for _ in range(n)]
    dist[0] = 1
    # 1から各都市への最短経路数を表す
    # 1からの距離が同じ都市の数を表す
    dist_cnt = [0 for _ in range(n)]
    dist_cnt[0] = 1
    # 1からの距離が1の都市をキューに入れる
    queue = [0]
    # 幅優先探索
    while len(queue) > 0:
        # 1からの距離が1の都市を取り出す
        x = queue.pop(0)
        # 1からの距離が1の都市に隣接する都市を調べる
        for y in road[x]:
            # 1からの距離が未確定の場合
            if dist[y] == 0:
                # 1からの距離を更新
                dist[y] = dist[x] + 1
                # 1からの距離が1の都市の数を更新
                dist_cnt[y] = dist_cnt[x]
                # 1からの距離が1の都市をキューに入れる
                queue.append(y)
            # 1からの距離が確定している場合
            elif dist[y] == dist[x] +

if __name__ == '__main__':
    main()