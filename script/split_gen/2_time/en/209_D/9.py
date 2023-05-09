def main():
    N, Q = map(int, input().split())
    # 各頂点について、その頂点からの距離を記録する
    distance = [-1] * N
    # 0番目の頂点は、0番目の頂点からの距離は0
    distance[0] = 0
    # 隣接リストを用意する
    edges = [[] for _ in range(N)]
    # 隣接リストに、各頂点の隣接する頂点を格納していく
    for _ in range(N-1):
        a, b = map(int, input().split())
        edges[a-1].append(b-1)
        edges[b-1].append(a-1)
    # 幅優先探索で、各頂点からの距離を計算する
    queue = [0]
    while queue:
        # 今いる頂点を取り出す
        now = queue.pop(0)
        # 今いる頂点から隣接する頂点を取り出していく
        for edge in edges[now]:
            # すでに距離が計算されている頂点はスキップする
            if distance[edge] != -1:
                continue
            # 距離を計算する
            distance[edge] = distance[now] + 1
            # 計算した頂点をqueueに追加する
            queue.append(edge)
    # 各クエリについて処理を行う
    for _ in range(Q):
        c, d = map(int, input().split())
        # cとdの距離が偶数なら、Townに到着する
        if (distance[c-1] + distance[d-1]) % 2 == 0:
            print('Town')
        # cとdの距離が奇数なら、Roadに到着する
        else:
            print('Road')
