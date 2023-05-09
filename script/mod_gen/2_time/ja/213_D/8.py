def main():
    # 都市数N
    N = int(input())
    # 都市間の道路
    road = [list(map(int, input().split())) for _ in range(N - 1)]
    # 道路のリストを作成
    road_list = [[] for _ in range(N + 1)]
    for i in range(N - 1):
        road_list[road[i][0]].append(road[i][1])
        road_list[road[i][1]].append(road[i][0])
    # 都市を訪れたかどうかのリスト
    visit = [0 for _ in range(N + 1)]
    # 都市を訪れた順番のリスト
    visit_order = []
    # 前にいた都市のリスト
    previous_city = [0 for _ in range(N + 1)]
    # 現在いる都市
    now_city = 1
    # 都市を訪れたかどうかのリストの初期化
    visit[now_city] = 1
    # 都市を訪れた順番のリストの初期化
    visit_order.append(now_city)
    # 都市を訪れたかどうかのリストの初期化
    while len(visit_order) < N:
        # 現在いる都市から行ける都市のうち、未訪問の都市を探す
        for i in range(len(road_list[now_city])):
            if visit[road_list[now_city][i]] == 0:
                # 前にいた都市のリストの更新
                previous_city[road_list[now_city][i]] = now_city
                # 現在いる都市の更新
                now_city = road_list[now_city][i]
                # 都市を訪れたかどうかのリストの更新
                visit[now_city] = 1
                # 都市を訪れた順番のリストの更新
                visit_order.append(now_city)
                break
        # 未訪問の都市がない場合
        else:

if __name__ == '__main__':
    main()