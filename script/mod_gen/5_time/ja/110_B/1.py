def main():
    # 標準入力からN, M, X, Yを取得する
    N, M, X, Y = map(int, input().split())
    # 標準入力からA帝国の都市の座標を取得する
    x_list = list(map(int, input().split()))
    # 標準入力からB帝国の都市の座標を取得する
    y_list = list(map(int, input().split()))
    # A帝国の都市の座標の最大値を取得する
    x_max = max(x_list)
    # B帝国の都市の座標の最小値を取得する
    y_min = min(y_list)
    # X < Z ≦ Y かつ x_1, x_2, ..., x_N < Z かつ y_1, y_2, ..., y_M ≧ Z を満たす整数Zが存在するかどうかを判定する
    if X < y_min and y_min <= Y and x_max < y_min:
        print("No War")
    else:
        print("War")

if __name__ == '__main__':
    main()