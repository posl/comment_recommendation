Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    Q = int(input())
    t, k = [], []
    for _ in range(Q):
        t_i, k_i = map(int, input().split())
        t.append(t_i)
        k.append(k_i)

    # 1回目の置換で何文字になるかを計算
    # A -> BC, B -> CA, C -> AB
    # 1回目の置換で何文字になるかを計算
    # A -> BC, B -> CA, C -> AB
    S1 = S.replace('A', 'B').replace('C', 'A').replace('B', 'C')

    # 2回目の置換で何文字になるかを計算
    # A -> BC, B -> CA, C -> AB
    S2 = S.replace('A', 'C').replace('B', 'A').replace('C', 'B')

    # 3回目の置換で何文字になるかを計算
    # A -> BC, B -> CA, C -> AB
    S3 = S.replace('B', 'C').replace('A', 'B').replace('C', 'A')

    # それぞれの置換で何文字になるかを計算
    # A -> BC, B -> CA, C -> AB
    S1 = S.replace('A', 'B').replace('C', 'A').replace('B', 'C')
    S2 = S.replace('A', 'C').replace('B', 'A').replace('C', 'B')
    S3 = S.replace('B', 'C').replace('A', 'B').replace('C', 'A')

    # 1回目の置換で何文字になるかを計算
    # A -> BC, B -> CA, C -> AB
    S1 = S.replace('A', 'B').replace('C', 'A').replace('B', 'C')

    # 2回目の置換で何文字になるかを計算
    # A -> BC, B -> CA, C -> AB
    S2 = S.replace('A', 'C').replace('B', 'A').

=======
Suggestion 2

def main():
    S = input()
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    A = S.count("A")
    B = S.count("B")
    C = S.count("C")
    for t, k in query:
        t %= (A + B + C)
        if t == 0:
            print(S[k - 1])
            continue
        for i in range(t):
            if S[k - 1] == "A":
                k += B
            elif S[k - 1] == "B":
                k += C
            else:
                k -= C
        print(S[k - 1])

=======
Suggestion 3

def main():
    s = input()
    q = int(input())
    for _ in range(q):
        t, k = map(int, input().split())
        if t % 3 == 0:
            print(s[(k - 1) % len(s)])
        elif t % 3 == 1:
            if k <= s.count("B"):
                print("B")
            elif k <= s.count("B") + s.count("C"):
                print("C")
            else:
                print("A")
        else:
            if k <= s.count("A"):
                print("A")
            elif k <= s.count("A") + s.count("B"):
                print("B")
            else:
                print("C")

=======
Suggestion 4

def main():
    s = input()
    q = int(input())
    for _ in range(q):
        t, k = map(int, input().split())
        if t % 3 == 0:
            print(s[(k - 1) % len(s)])
        elif t % 3 == 1:
            if s[(k - 1) % len(s)] == 'A':
                print('B')
            elif s[(k - 1) % len(s)] == 'B':
                print('C')
            else:
                print('A')
        else:
            if s[(k - 1) % len(s)] == 'A':
                print('C')
            elif s[(k - 1) % len(s)] == 'B':
                print('A')
            else:
                print('B')

=======
Suggestion 5

def main():
    s = input()
    q = int(input())
    for i in range(q):
        t, k = map(int, input().split())
        if t % 3 == 0:
            print(s[(k - 1) % len(s)])
        elif t % 3 == 1:
            if s[(k - 1) % len(s)] == 'A':
                print('B')
            elif s[(k - 1) % len(s)] == 'B':
                print('C')
            elif s[(k - 1) % len(s)] == 'C':
                print('A')
        elif t % 3 == 2:
            if s[(k - 1) % len(s)] == 'A':
                print('C')
            elif s[(k - 1) % len(s)] == 'B':
                print('A')
            elif s[(k - 1) % len(s)] == 'C':
                print('B')

=======
Suggestion 6

def main():
    S = input()
    Q = int(input())
    queries = [list(map(int, input().split())) for _ in range(Q)]

    # A, B, C のみからなる文字列 S が与えられます。
    # S^{(0)}:=S とし、i=1,2,3,... について S^{(i)} を S^{(i-1)} の各文字を A → BC, B → CA, C → AB と同時に置き換えたものと定義します。
    # 以下の Q 個のクエリに答えてください。i 個目のクエリの内容は以下の通りです。
    # S^{(t_i)} の先頭から k_i 文字目を出力せよ。
    # 入力例 1
    # ABC
    # 4
    # 0 1
    # 1 1
    # 1 3
    # 1 6
    # 出力例 1
    # A
    # B
    # C
    # B
    # S^{(0)}=ABC, S^{(1)}=BCCAAB です。
    # よって各クエリへの答えは順に A, B, C, B となります。
    # 入力例 2
    # CBBAACCCCC
    # 5
    # 57530144230160008 659279164847814847
    # 29622990657296329 861239705300265164
    # 509705228051901259 994708708957785197
    # 176678501072691541 655134104344481648
    # 827291290937314275 407121144297426665
    # 出力例 2
    # A
    # A
    # C
    # A
    # A

    # S は A, B, C のみからなる長さ 1 以上 10^5 以下の文字列
    # 1 ≦ Q ≦ 10^5
    #

=======
Suggestion 7

def main():
    S = input()
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    cnt = [0, 0, 0]
    for i in range(3):
        cnt[i] = S.count(chr(ord('A') + i))
    for t, k in query:
        t %= 3
        if t == 0:
            print(S[k - 1])
        else:
            k -= 1
            k = (k + cnt[t - 1]) % (cnt[0] + cnt[1] + cnt[2])
            if k < cnt[0]:
                print('A')
            elif k < cnt[0] + cnt[1]:
                print('B')
            else:
                print('C')

=======
Suggestion 8

def main():
    S = input()
    Q = int(input())
    for i in range(Q):
        t, k = map(int, input().split())
        s = S
        while t > 0:
            s = s.replace('A', 'BC').replace('B', 'CA').replace('C', 'AB')
            t -= 1
        print(s[k-1])

=======
Suggestion 9

def main():
    S = input()
    Q = int(input())
    t_k = [list(map(int, input().split())) for _ in range(Q)]
    #print(S, Q, t_k)
    #print(S[0], S[1], S[2])
    #print(S[3], S[4], S[5])
    #print(S[6], S[7], S[8])
    #print(S[9], S[10], S[11])
    #print(S[12], S[13], S[14])

    #S = input()
    #Q = int(input())
    #t_k = [list(map(int, input().split())) for _ in range(Q)]
    #print(S, Q, t_k)
    #print(S[0], S[1], S[2])
    #print(S[3], S[4], S[5])
    #print(S[6], S[7], S[8])
    #print(S[9], S[10], S[11])
    #print(S[12], S[13], S[14])

    #print(S[0], S[1], S[2])
    #print(S[3], S[4], S[5])
    #print(S[6], S[7], S[8])
    #print(S[9], S[10], S[11])
    #print(S[12], S[13], S[14])

    #print(S[0], S[1], S[2])
    #print(S[3], S[4], S[5])
    #print(S[6], S[7], S[8])
    #print(S[9], S[10], S[11])
    #print(S[12], S[13], S[14])

    #print(S[0], S[1], S[2])
    #print(S[3], S[4], S[5])
    #print(S[6], S[7], S[8])
    #print(S[9], S[10], S[11])
    #print(S[12], S[13], S[14])

    #print(S[0], S[1], S[2])
    #print(S[3], S[4], S[5])
    #print(S[6], S[7

=======
Suggestion 10

def main():
    s = input()
    q = int(input())
    # 3回目の置換で元の文字列に戻る
    s = s * 3
    # 置換の回数
    t = 0
    # 置換の回数と文字列の長さのペア
    d = {}
    # 置換の回数と文字列の長さのペアを作成
    for i in range(3):
        t += 1
        d[t] = len(s)
        s = s.replace('A', 'BC').replace('B', 'CA').replace('C', 'AB')
    # 置換の回数と文字列の長さのペアを作成
    for i in range(q):
        t, k = map(int, input().split())
        # 置換の回数が3回以上の場合は、置換の回数を3で割った余りに置換する
        if t > 3:
            t %= 3
        # 置換の回数が1の場合
        if t == 1:
            print(s[k - 1])
        # 置換の回数が2の場合
        elif t == 2:
            print(s[k + d[1] - 1])
        # 置換の回数が3の場合
        else:
            print(s[k + d[2] - 1])
