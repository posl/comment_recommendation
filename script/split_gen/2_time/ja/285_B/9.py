def main():
    #入力
    N = int(input())
    S = input()
    #N-1回繰り返す
    for i in range(1, N):
        #lの初期値はN-1
        l = N-1
        #lが0になるまで繰り返す
        while l > 0:
            #Sのi文字目をS_iとする
            S_i = S[i-1]
            #Sのl文字目をS_lとする
            S_l = S[l-1]
            #S_iとS_lが等しい場合
            if S_i == S_l:
                #lを1減らす
                l -= 1
            #S_iとS_lが等しくない場合
            else:
                #l+iがNを超える場合
                if l+i > N:
                    #lを1減らす
                    l -= 1
                #l+iがNを超えない場合
                else:
                    #Sのl+i文字目をS_l_iとする
                    S_l_i = S[l+i-1]
                    #S_lとS_l_iが等しい場合
                    if S_l == S_l_i:
                        #lを1減らす
                        l -= 1
                    #S_lとS_l_iが等しくない場合
                    else:
                        #ループを抜ける
                        break
        #結果を出力
        print(l)
