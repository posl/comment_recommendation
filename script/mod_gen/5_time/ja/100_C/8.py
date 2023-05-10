def main():
    # 標準入力から値を取得してinput_lineに入れる
    input_line = input()
    # input_lineをスペースで区切ってinput_line_splitに入れる
    input_line_split = input_line.split()
    # input_line_splitの要素をintに変換してinput_line_intに入れる
    input_line_int = [int(i) for i in input_line_split]
    # Nを取得
    N = input_line_int[0]
    # aを取得
    a = input_line_int[1:]
    # 操作回数
    count = 0
    # aの要素を順番に操作し、全ての要素が偶数になるまで操作を繰り返す
    while all(i % 2 == 0 for i in a):
        a = [i / 2 for i in a]
        count += 1
    # 操作回数を出力
    print(count)

if __name__ == '__main__':
    main()