def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a - 1 for a in A]
    # 町1からの移動経路のリスト
    route = [0]
    # 町1からの移動経路のリストのループの開始位置
    loop_start = 0
    # 町1からの移動経路のリストのループの長さ
    loop_len = 0
    # 開始位置からの移動回数
    move_count = 0
    # 町1からの移動経路のリストのループの開始位置の移動回数
    loop_start_move_count = 0
    # 町1からの移動経路のリストのループの開始位置の移動回数のリスト
    loop_start_move_count_list = []
    while True:
        # 町1からの移動経路のリストのループの開始位置を更新
        loop_start = len(route)
        # 町1からの移動経路のリストのループの開始位置の移動回数を更新
        loop_start_move_count = move_count
        # 町1からの移動経路のリストのループの開始位置の移動回数のリストに追加
        loop_start_move_count_list.append(loop_start_move_count)
        # 町1からの移動経路のリストに次の町を追加
        route.append(A[route[-1]])
        # 開始位置からの移動回数を更新
        move_count += 1
        # 町1からの移動経路のリストにループがある場合
        if route[-1] in route[:-1]:
            # 町1からの移動経路のリストのループの長さを計算
            loop_len = len(route) - route.index(route[-1]) - 1
            # 移動

if __name__ == '__main__':
    main()