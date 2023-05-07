def main():
    # 標準入力から値を取得してinput_lineに入れる
    input_line1 = input()
    input_line2 = input()
    input_line3 = input()
    # スペースで分割して、input_line1,input_line2,input_line3に再代入
    S,T = input_line1.split()
    A,B = input_line2.split()
    U = input_line3
    # 出力
    if U == S:
        print(int(A)-1, int(B))
    else:
        print(int(A), int(B)-1)
