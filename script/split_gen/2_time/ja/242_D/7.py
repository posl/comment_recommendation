def main():
    S = input()
    Q = int(input())
    #SのA,B,Cの数を数える
    A = S.count('A')
    B = S.count('B')
    C = S.count('C')
    #Sの長さ
    Slen = len(S)
    for i in range(Q):
        t, k = map(int, input().split())
        #Sの長さを超える場合は周期で割る
        if t >= Slen:
            t = t % Slen
        #tが0の場合は、Sのk-1文字目を出力
        if t == 0:
            print(S[k-1])
        #tが0ではない場合は、
        else:
            #tがAの数を超える場合は、Aの数を周期で割った余りをtとする
            if t > A:
                t = t % A
            #tがBの数を超える場合は、Bの数を周期で割った余りをtとする
            if t > B:
                t = t % B
            #tがCの数を超える場合は、Cの数を周期で割った余りをtとする
            if t > C:
                t = t % C
            #tの数だけSを回す
            for j in range(t):
                #Sのk-1文字目を出力
                print(S[k-1])
                #k-1文字目をSのk文字目に置き換える
                S = S[:k-1] + S[k]
                #Sの長さを更新する
                Slen = len(S)
