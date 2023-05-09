def main():
    # 標準入力から値を取得してinput_lineに入れる
    input_line = input()
    # input_lineを半角スペースで分割して、input_lineに上書き
    input_line = input_line.split(" ")
    # input_lineをint型に変換して、input_lineに上書き
    input_line = list(map(int, input_line))
    # input_lineの各要素を変数に代入
    N = input_line[0]
    x = input_line[1]
    y = input_line[2]
    h = input_line[3]
    # ここから問題を解く
    # N個の情報から、中心座標と高さを特定する
    # その中心座標と高さを出力する
    for i in range(N):
        input_line = input()
        input_line = input_line.split(" ")
        input_line = list(map(int, input_line))
        x_i = input_line[0]
        y_i = input_line[1]
        h_i = input_line[2]
        if h_i > 0:
            cx = x_i
            cy = y_i
            ch = h_i
    print(cx, cy, ch)

if __name__ == '__main__':
    main()