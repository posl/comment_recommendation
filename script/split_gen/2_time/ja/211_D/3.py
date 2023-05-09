def main():
    N, M = map(int, input().split())
    # 隣接リスト
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)
    # 都市 1 から都市 N への移動に必要な時間
    time = [-1] * N
    # 都市 1 から都市 N への移動に必要な時間の最小値
    min_time = -1
    # 都市 1 から都市 N への移動に必要な時間の最小値を実現する経路の数
    min_time_path = 0
    # 幅優先探索
    que = [0]
    time[0] = 0
    while que:
        # キューの先頭を取り出す
        v = que.pop(0)
        # キューの先頭から移動可能な都市を順に探索
        for nv in graph[v]:
            # まだ探索していない都市の場合
            if time[nv] == -1:
                # キューの末尾に追加
                que.append(nv)
                # その都市に移動するのに必要な時間を更新
                time[nv] = time[v] + 1
                # 最小値を更新した場合
                if min_time == -1 or time[nv] < min_time:
                    min_time = time[nv]
                    min_time_path = 1
                # 最小値と同じ場合
                elif time[nv] == min_time:
                    min_time_path += 1
    print(min_time_path)
