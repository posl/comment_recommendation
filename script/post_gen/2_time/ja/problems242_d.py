Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    Q = int(input())
    t = [0] * Q
    k = [0] * Q
    for i in range(Q):
        t[i], k[i] = map(int, input().split())
    #print(S, Q, t, k)
    #print(S[0])
    #print(S[1])
    #print(S[2])
    #print(S[3])
    #print(S[4])
    #print(S[5])
    #print(S[6])
    #print(S[7])
    #print(S[8])
    #print(S[9])
    #print(S[10])
    #print(S[11])
    #print(S[12])
    #print(S[13])
    #print(S[14])
    #print(S[15])
    #print(S[16])
    #print(S[17])
    #print(S[18])
    #print(S[19])
    #print(S[20])
    #print(S[21])
    #print(S[22])
    #print(S[23])
    #print(S[24])
    #print(S[25])
    #print(S[26])
    #print(S[27])
    #print(S[28])
    #print(S[29])
    #print(S[30])
    #print(S[31])
    #print(S[32])
    #print(S[33])
    #print(S[34])
    #print(S[35])
    #print(S[36])
    #print(S[37])
    #print(S[38])
    #print(S[39])
    #print(S[40])
    #print(S[41])
    #print(S[42])
    #print(S[43])
    #print(S[44])
    #print(S[45])
    #print(S[46])
    #print(S[47])
    #print(S[48])
    #print(S[49])
    #print(S[50])
    #print(S[51])
    #print(S[52])
    #print(S[53])
    #print(S[54])
    #print(S[55])
    #print(S[56])
    #print(S[57])
    #print(S[58])
    #print(S[59])
    #print(S[60])
    #print(S[61])
    #

=======
Suggestion 2

def main():
    S = input()
    Q = int(input())
    T = []
    K = []
    for _ in range(Q):
        t, k = map(int, input().split())
        T.append(t)
        K.append(k)
    A = S.count('A')
    B = S.count('B')
    C = S.count('C')
    for i in range(Q):
        t = T[i]
        k = K[i]
        if t % 3 == 0:
            if k <= A:
                print('A')
            elif k <= A + B:
                print('B')
            else:
                print('C')
        elif t % 3 == 1:
            if k <= B:
                print('B')
            elif k <= A + B:
                print('C')
            else:
                print('A')
        else:
            if k <= C:
                print('C')
            elif k <= A + C:
                print('A')
            else:
                print('B')

main()

=======
Suggestion 3

def main():
    S = input()
    Q = int(input())
    t = []
    k = []
    for i in range(Q):
        t_i, k_i = map(int, input().split())
        t.append(t_i)
        k.append(k_i)

    # A, B, C のみからなる文字列 S が与えられます。
    # S^{(0)}:=S とし、i=1,2,3,... について S^{(i)} を S^{(i-1)} の各文字を A → BC, B → CA, C → AB と同時に置き換えたものと定義します。
    # 以下の Q 個のクエリに答えてください。i 個目のクエリの内容は以下の通りです。
    # S^{(t_i)} の先頭から k_i 文字目を出力せよ。
    # 制約
    # S は A, B, C のみからなる長さ 1 以上 10^5 以下の文字列
    # 1 ≦ Q ≦ 10^5
    # 0 ≦ t_i ≦ 10^{18}
    # 1 ≦ k_i ≦ min(10^{18}, S^{(t_i)} の長さ)
    # Q, t_i, k_i は整数

    # 文字列の長さを取得
    N = len(S)
    # 文字列の長さの最大値を取得
    N_max = 10 ** 5
    # t_i の最大値を取得
    t_max = 10 ** 18
    # 文字列の長さの最大値を取得
    N_min = 1
    # t_i の最小値を取得
    t_min = 0
    # k_i の最大値を取得
    k_max = min(10 ** 18, N)
    # k_i の最小値を取得
    k_min = 1

    # 文字列の長さを取得
    if not (

=======
Suggestion 4

def main():
    S = input()
    Q = int(input())
    for i in range(Q):
        t, k = map(int, input().split())
        if t % 3 == 0:
            print(S[(k-1) % len(S)])
        elif t % 3 == 1:
            if S[(k-1) % len(S)] == 'A':
                print('B')
            elif S[(k-1) % len(S)] == 'B':
                print('C')
            else:
                print('A')
        else:
            if S[(k-1) % len(S)] == 'A':
                print('C')
            elif S[(k-1) % len(S)] == 'B':
                print('A')
            else:
                print('B')

=======
Suggestion 5

def main():
    s = input()
    q = int(input())
    n = len(s)
    cnt = [0] * 3
    for i in range(n):
        cnt[ord(s[i]) - ord('A')] += 1
    for _ in range(q):
        t, k = map(int, input().split())
        t %= 3
        if t == 0:
            if k <= cnt[0]:
                print('A')
            elif k <= cnt[0] + cnt[1]:
                print('B')
            else:
                print('C')
        elif t == 1:
            if k <= cnt[1]:
                print('B')
            elif k <= cnt[0] + cnt[1]:
                print('C')
            else:
                print('A')
        else:
            if k <= cnt[2]:
                print('C')
            elif k <= cnt[0] + cnt[2]:
                print('A')
            else:
                print('B')

=======
Suggestion 6

def main():
    S = input()
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    #S = "CBBAACCCCC"
    #query = [[57530144230160008, 659279164847814847], [29622990657296329, 861239705300265164], [509705228051901259, 994708708957785197], [176678501072691541, 655134104344481648], [827291290937314275, 407121144297426665]]
    #print(S, query)
    #print(S[0])
    #print(len(S))
    #print(S[0:2])
    #print(S[2:4])
    #print(S[4:6])
    #print(S[6:8])
    #print(S[8:10])
    #print(S[10:12])
    #print(S[12:14])
    #print(S[14:16])
    #print(S[16:18])
    #print(S[18:20])
    #print(S[20:22])
    #print(S[22:24])
    #print(S[24:26])
    #print(S[26:28])
    #print(S[28:30])
    #print(S[30:32])
    #print(S[32:34])
    #print(S[34:36])
    #print(S[36:38])
    #print(S[38:40])
    #print(S[40:42])
    #print(S[42:44])
    #print(S[44:46])
    #print(S[46:48])
    #print(S[48:50])
    #print(S[50:52])
    #print(S[52:54])
    #print(S[54:56])
    #print(S[56:58])
    #print(S[58:60])
    #print(S[60:62])
    #print(S[62:64])
    #print(S[64:66])
    #print(S[66:68])
    #print(S[68:70])
    #print(S[70:72])
    #print(S[72:74])
    #print(S[74:76])
    #print(S[76:78])
    #print(S

=======
Suggestion 7

def main():
    S = input()
    Q = int(input())
    queries = [list(map(int, input().split())) for _ in range(Q)]
    #print(S)
    #print(Q)
    #print(queries)
    #S = 'ABC'
    #Q = 4
    #queries = [[0, 1], [1, 1], [1, 3], [1, 6]]
    #print(S)
    #print(Q)
    #print(queries)
    #S = 'CBBAACCCCC'
    #Q = 5
    #queries = [[57530144230160008, 659279164847814847], [29622990657296329, 861239705300265164], [509705228051901259, 994708708957785197], [176678501072691541, 655134104344481648], [827291290937314275, 407121144297426665]]
    #print(S)
    #print(Q)
    #print(queries)
    #S = 'ABC'
    #Q = 4
    #queries = [[0, 1], [1, 1], [1, 3], [1, 6]]
    #print(S)
    #print(Q)
    #print(queries)
    #S = 'CBBAACCCCC'
    #Q = 5
    #queries = [[57530144230160008, 659279164847814847], [29622990657296329, 861239705300265164], [509705228051901259, 994708708957785197], [176678501072691541, 655134104344481648], [827291290937314275, 407121144297426665]]
    #print(S)
    #print(Q)
    #print(queries)

    #S = 'ABC'
    #Q = 4
    #queries = [[0, 1], [1, 1], [1, 3], [1, 6]]
    #print(S)
    #print(Q)
    #print(queries)
    #S = 'CBBAACCCCC'
    #Q = 5
    #queries = [[57530144230160008, 659279164847814847], [29622990657296329,

=======
Suggestion 8

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

=======
Suggestion 9

def main():
    S = input()
    Q = int(input())
    query = []
    for i in range(Q):
        t,k = map(int,input().split())
        query.append([t,k])
    
    #Sの各文字をA→BC,B→CA,C→ABと置き換える
    #A→BC,B→CA,C→AB
    #A→B,B→C,C→A
    #A→1,B→2,C→3
    #1→B,2→C,

=======
Suggestion 10

def main():
    s = input()
    q = int(input())
    l = []
    for i in range(q):
        l.append(input().split())
    #print(l)
    #print(s)
    #print(q)
    for i in range(q):
        t = int(l[i][0])
        k = int(l[i][1])
        #print(t,k)
        if t%3 == 0:
            print(s[k-1])
        elif t%3 == 1:
            if k <= len(s)//3:
                print(s[k-1])
            elif k <= len(s)//3*2:
                print(s[len(s)//3*2+k-1])
            else:
                print(s[k-1])
        else:
            if k <= len(s)//3:
                print(s[len(s)//3*2+k-1])
            elif k <= len(s)//3*2:
                print(s[k-1])
            else:
                print(s[len(s)//3*2+k-1])
