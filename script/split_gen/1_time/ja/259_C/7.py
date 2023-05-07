def main():
    S = input()
    T = input()
    #Sの文字列の長さを取得
    S_length = len(S)
    #Sの文字列の長さ分ループ
    for i in range(S_length):
        #Sの文字列の長さ-1とiが等しい場合
        if S_length-1 == i:
            #Sの文字列にTの文字列を追加
            S += T
            #ループを抜ける
            break
        #Sのi文字目とi+1文字目が等しい場合
        if S[i] == S[i+1]:
            #Sのi文字目とi+1文字目の間にTのi文字目を追加
            S = S[:i+1] + T[i] + S[i+1:]
            #ループを抜ける
            break
    #SとTが等しい場合
    if S == T:
        #Yesを出力
        print("Yes")
    #SとTが等しくない場合
    else:
        #Noを出力
        print("No")
