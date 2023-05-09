def main():
    S = input()
    T = input()
    #Tを一文字ずつ見ていく
    #Tの文字数分だけ回す
    for i in range(len(T)):
        #Tのi文字目とSのi文字目が違う場合
        if T[i] != S[i]:
            #Tのi文字目がSのi+1文字目と一致する場合
            if T[i] == S[i+1]:
                #Tのi文字目とSのi+1文字目を入れ替える
                S = S[:i+1] + T[i] + S[i+1:]
            #違う場合
            else:
                #Noを出力して終了
                print("No")
                return
    #Yesを出力して終了
    print("Yes")
