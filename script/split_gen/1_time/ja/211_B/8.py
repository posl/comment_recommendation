def main():
    #文字列の入力
    #文字列の入力
    S_1 = input()
    S_2 = input()
    S_3 = input()
    S_4 = input()
    #文字列のリスト化
    S = [S_1,S_2,S_3,S_4]
    #リストの中の文字列の数をカウント
    H = S.count("H")
    B2 = S.count("2B")
    B3 = S.count("3B")
    HR = S.count("HR")
    #文字列の数が1ならYes、それ以外ならNoを出力
    if H == 1 and B2 == 1 and B3 == 1 and HR == 1:
        print("Yes")
    else:
        print("No")
