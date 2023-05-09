def main():
    # 標準入力から N, T を取得
    N, T = map(int, input().split())
    # 標準入力から N 個の経路を取得し、リストに格納
    routes = [list(map(int, input().split())) for _ in range(N)]
    # 最小コストを格納する変数
    min_cost = float("inf")
    # 経路を1つずつ取り出す
    for route in routes:
        # 経路のコストと時間を取得
        cost, time = route
        # 経路の時間が T 以内であれば
        if time <= T:
            # 経路のコストを最小コストと比較し、もし経路のコストが小さければ
            if cost < min_cost:
                # 最小コストを更新
                min_cost = cost
    # 最小コストが更新されていれば
    if min_cost != float("inf"):
        # 最小コストを出力
        print(min_cost)
    # 最小コストが更新されていなければ
    else:
        # TLE を出力
        print("TLE")

if __name__ == '__main__':
    main()