def main():
    N, M = map(int, input().split())
    # 駒が置かれているマス
    x = 0
    y = 0
    # 駒が置かれているマスからの距離
    distance = [[0]*N for _ in range(N)]
    # 駒が置かれているマスからの距離がMの倍数かどうか
    is_m = [[False]*N for _ in range(N)]
    # 駒が置かれているマスからの距離がMの倍数のマスの数
    count = 0
    # 駒が置かれているマスからの距離がMの倍数のマスの数がN*Nになるまで繰り返す
    while count < N*N:
        # 駒が置かれているマスからの距離がMの倍数でなければ更新
        if not is_m[y][x]:
            is_m[y][x] = True
            count += 1
        # 駒が置かれているマスからの距離がMの倍数であれば更新
        else:
            distance[y][x] += 1
        # 駒が置かれているマスからの距離がMの倍数でなければ更新
        if not is_m[y][x]:
            is_m[y][x] = True
            count += 1
        # 駒が置かれているマスからの距離がMの倍数であれば更新
        else:
            distance[y][x] += 1
        # 駒が置かれているマスからの距離がMの倍数でなければ更新
        if not is_m[y][x]:
            is_m[y][x] = True
            count += 1
        # 駒が置かれているマスからの距離がMの倍数であれば更新

if __name__ == '__main__':
    main()