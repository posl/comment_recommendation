def main():
    # 座標入力
    print("座標を入力してください")
    A_x, A_y = map(int, input().split())
    B_x, B_y = map(int, input().split())
    C_x, C_y = map(int, input().split())
    D_x, D_y = map(int, input().split())
    # 座標をリストにまとめる
    x_list = [A_x, B_x, C_x, D_x]
    y_list = [A_y, B_y, C_y, D_y]
    # 座標の最大値と最小値を求める
    x_max = max(x_list)
    x_min = min(x_list)
    y_max = max(y_list)
    y_min = min(y_list)
    # 最大値と最小値の差を求める
    x_diff = x_max - x_min
    y_diff = y_max - y_min
    # 差が0の場合、四角形ではない
    if x_diff == 0 or y_diff == 0:
        print("No")
        return
    # 差が0でない場合、四角形である
    # 正方形の場合、四角形であるが凸ではない
    # 四角形であるが凸ではない場合、凸ではない
    print("Yes")
