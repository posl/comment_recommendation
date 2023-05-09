def main():
    # スペース区切りの整数の入力
    C = input()
    # 文字列をリストに格納
    C_list = list(C)
    # 全て同じ文字ならWon
    if C_list[0] == C_list[1] == C_list[2]:
        print('Won')
    else:
        print('Lost')
