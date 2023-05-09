def main():
    #入力
    S = []
    for i in range(10):
        S.append(input())
    #print(S)
    #print(S[0])
    #処理
    #まず、 S_i (1 ≦ i ≦ 10)= .......... ( . が 10 個並んだ文字列) とする。
    #次に、以下の条件を全て満たす 4 つの整数 A,B,C,D を選ぶ。
    #1 ≦ A ≦ B ≦ 10
    #1 ≦ C ≦ D ≦ 10
    #その後、以下の条件を全て満たす全ての整数組 (i,j) について、 S_i の j 文字目を # に書き換える。
    #A ≦ i ≦ B
    #C ≦ j ≦ D
    #print(S[0][0])
    #print(S[0][1])
    #print(S[0][2])
    #print(S[0][3])
    #print(S[0][4])
    #print(S[0][5])
    #print(S[0][6])
    #print(S[0][7])
    #print(S[0][8])
    #print(S[0][9])
    #A,B,C,Dを決定
    A = 0
    B = 0
    C = 0
    D = 0
    for i in range(10):
        for j in range(10):
            if(S[i][j] == "#"):
                if(A == 0):
                    A = i + 1
                if(B < i + 1):
                    B = i + 1
                if(C == 0):
                    C = j + 1
                if(D < j + 1):
                    D = j + 1
    #出力
    print(A,B)
    print(C,D)

if __name__ == '__main__':
    main()