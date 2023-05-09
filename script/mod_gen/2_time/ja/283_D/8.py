def main():
    #入力
    S = input()
    #Sの長さ
    N = len(S)
    #Sをリストに変換
    S = list(S)
    #箱
    box = []
    #高橋君の気を失うかどうかの判定
    flag = 0
    #i = 1,2, ... ,|S| に対してこの順に気を失わない限り操作を行います。
    for i in range(N):
        #S_i が英小文字ならば、その英小文字が書かれたボールを箱に入れる。ただし、そのボールがすでに箱に入っている場合、高橋君は気を失う。
        if (S[i].islower()):
            #ボールがすでに箱に入っているかどうかの判定
            if (S[i] in box):
                print("No")
                break
            else:
                box.append(S[i])
        #S_i が ( ならば、何もしない。  
        elif (S[i] == "("):
            continue
        #S_i が ) ならば、i 未満の整数 j であって、S の j 番目から i 番目までの文字からなる文字列が良い文字列となる最大の整数 j を取る。（このような整数 j は必ず存在することが証明できる。）j 番目から i 番目までの操作で箱に入れたボールをすべて、箱から取り出す。
        else:
            for j in range(i-1,-1,-1):
                if (S[j] == "("):
                    #箱に入れたボールをすべて、箱から取り出す
                    for k in range(j+1,i):
                        if (S[k] in box):
                            box.remove(S[k])
                        else:
                            print("No")
                            flag = 1
                            break
                    #箱

if __name__ == '__main__':
    main()