def main():
    N, Q = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N - 1)]
    CD = [list(map(int, input().split())) for _ in range(Q)]
    graph = [[] for _ in range(N + 1)]
    for a, b in AB:
        graph[a].append(b)
        graph[b].append(a)
    #print(graph)
    #print(CD)
    # 頂点1からの最短距離を求める
    # 始点を1とする
    s = 1
    # 各頂点の最短距離を格納する配列
    dist = [-1] * (N + 1)
    # 始点の距離を0とする
    dist[s] = 0
    # BFS用のキューを用意
    que = [s]
    # BFS開始
    while que:
        # キューから頂点を取り出す
        v = que.pop(0)
        # 頂点vから辿れる頂点を全て調べる
        for nv in graph[v]:
            # すでに最短距離が求まっているならスルー
            if dist[nv] != -1:
                continue
            # 新たな頂点なので距離を記録してキューに入れる
            dist[nv] = dist[v] + 1
            que.append(nv)
    #print(dist)
    for c, d in CD:
        if (dist[c] + dist[d]) % 2 == 0:
            print('Town')
        else:
            print('Road')

if __name__ == '__main__':
    main()