def main():
    S = input()
    T = input()
    # 文字列の長さを取得
    str_len = len(S)
    # 文字列の長さ分ループ
    for i in range(str_len):
        # 1文字目と2文字目を入れ替える
        S = S[1:] + S[0]
        # 入れ替えた文字列とTが一致しているか確認
        if S == T:
            print("Yes")
            exit()
    # 1文字目と2文字目を入れ替えても一致しなかった場合
    print("No")
