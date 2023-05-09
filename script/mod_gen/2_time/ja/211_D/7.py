def main():
    N, M = map(int, input().split())
    # 都市間の道路情報を格納するリスト
    roadlist = [[] for i in range(N)]
    # 道路数が0の場合は0を出力
    if M == 0:
        print(0)
        return
    # 道路情報をリストに格納
    for i in range(M):
        a, b = map(int, input().split())
        roadlist[a - 1].append(b - 1)
        roadlist[b - 1].append(a - 1)
    # 都市1から都市Nへの最短経路を格納するリスト
    shortest = [0] * N
    # 都市1から都市Nへの最短経路の数を格納するリスト
    shortestcount = [0] * N
    # 都市1から都市Nへの最短経路の数を格納するリストの初期値を1にする
    shortestcount[0] = 1
    # 都市1から都市Nへの最短経路を探索する
    for i in range(N):
        # 都市1から都市Nへの最短経路が探索済みの場合は処理をスキップ
        if shortest[i] != 0:
            continue
        # 都市1から都市Nへの最短経路を探索する
        for j in range(N):
            # 都市1から都市Nへの最短経路を探索済みの場合は処理をスキップ
            if shortest[j] != 0:
                continue
            # 都市1から都市Nへの最短経路が探索済みの場合は処理をスキップ
            if shortestcount[j] != 0:
                continue
            # 都市1から都市N

if __name__ == '__main__':
    main()