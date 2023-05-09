def main():
    N, M = map(int, input().split())
    # 都市の数だけ0のリストを用意する
    city = [0] * N
    # 都市の数だけ、その都市に到達できる都市のリストを用意する
    city_list = [[] for i in range(N)]
    # 道路の数だけ、道路の両端の都市を取得する
    for i in range(M):
        A, B = map(int, input().split())
        # 都市のリストに、到達できる都市を追加する
        city_list[A-1].append(B-1)
    # 都市の数だけ繰り返す
    for i in range(N):
        # 都市のリストを繰り返す
        for j in city_list[i]:
            # 都市のリストの中身を繰り返す
            for k in city_list[j]:
                # 到達できる都市が、その都市自身でなければ、
                # その都市に到達できる都市のリストに追加する
                if k != i:
                    city_list[i].append(k)
    # 都市の数だけ繰り返す
    for i in range(N):
        # 都市のリストの重複を削除する
        city_list[i] = list(set(city_list[i]))
        # 都市のリストの数を、都市のリストの数だけ増やす
        city[i] = len(city_list[i])
    # 都市の数の2乗を出力する
    print(sum(city) ** 2)
