def main():
    #文字列の入力
    S = input()
    #print(S)
    #文字列の長さ
    length = len(S)
    #print(length)
    #文字列の中にある?の数
    Q = S.count('?')
    #print(Q)
    #ABC数
    ABC = 0
    #?の数が0の場合は、Sの中にABCが何個あるかを調べる
    if Q == 0:
        #print('Q = 0')
        #Sの中にABCが何個あるかを調べる
        for i in range(length-2):
            if S[i] == 'A':
                if S[i+1] == 'B':
                    if S[i+2] == 'C':
                        ABC += 1
        #print(ABC)
        #ABC数を10^9 + 7で割った余りを出力
        print(ABC % (10**9 + 7))
    #?の数が0より大きい場合は、Sの中に?があるところにA,B,Cを入れてABC数を求める
    else:
        #print('Q > 0')
        #?があるところにA,B,Cを入れてABC数を求める
        for i in range(3**Q):
            #print('i = ' + str(i))
            #Sの中に?があるところにA,B,Cを入れる
            for j in range(Q):
                #print('j = ' + str(j))
                #print('i // (3**j) % 3 = ' + str(i // (3**j) % 3))
                S = S.replace('?', 'A', 1)
                S = S.replace('?', 'B', 1)
                S = S.replace('?', 'C', 1)
            #print(S)
            #Sの中にABCが何個あるかを調べる
            for k in range(length-2):
                if S[k] == 'A':
                    if S[k+1] == 'B':
                        if S[k+2]

if __name__ == '__main__':
    main()