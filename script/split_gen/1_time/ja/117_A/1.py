def main():
    # 標準入力から値を取得してinput_lineに入れる
    input_line = input()
    # input_lineの値をスペースで区切ってリストに入れる
    input_list = input_line.split()
    # リストの値を変数に入れる
    time = int(input_list[0])
    x = int(input_list[1])
    # 出力
    print(time/x)
