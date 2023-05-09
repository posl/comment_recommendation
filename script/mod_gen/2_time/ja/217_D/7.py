def main():
    L, Q = map(int, input().split())
    # クエリの種類と位置を格納する
    query = [list(map(int, input().split())) for _ in range(Q)]
    # 木の長さを格納する
    wood = [L]
    for i in range(Q):
        # クエリの種類が2のとき
        if query[i][0] == 2:
            # 木の長さを出力する
            print(wood[query[i][1] - 1])
        # クエリの種類が1のとき
        else:
            # 木の長さを更新する
            wood = update(wood, query[i][1])
    return

if __name__ == '__main__':
    main()