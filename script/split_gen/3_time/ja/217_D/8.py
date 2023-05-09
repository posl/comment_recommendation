def main():
    L, Q = map(int, input().split())
    # 線の位置を格納するリストを作成
    line_list = [0, L]
    # クエリに対する処理
    for i in range(Q):
        c_i, x_i = map(int, input().split())
        # 線を引く場合
        if c_i == 1:
            line_list.append(x_i)
        # 線を引く場合
        elif c_i == 2:
            # 線の位置を昇順にソート
            line_list.sort()
            # 線の位置の中で、線を引く位置よりも大きい値の最小のインデックスを取得
            index = line_list.index(x_i)
            # 線を引く位置よりも小さい値と大きい値の差を出力
            print(line_list[index] - line_list[index-1])
