Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if sorted(S[i]) == sorted(S[j]):
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            if sorted(S[i]) == sorted(S[j]):
                ans += 1
    print(ans)

main()

=======
Suggestion 3

def main():
    N = int(input())
    s = [input() for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if sorted(s[i]) == sorted(s[j]):
                count += 1
    print(count)

=======
Suggestion 4

def main():
    N = int(input())
    S = [input() for i in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(i + 1, N):
            if sorted(S[i]) == sorted(S[j]):
                cnt += 1
    print(cnt)

=======
Suggestion 5

def solve():
    N = int(input())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if sorted(S[i]) == sorted(S[j]):
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S = [sorted(s) for s in S]
    S = [''.join(s) for s in S]
    S = sorted(S)
    ans = 0
    i = 0
    while i < N:
        j = i
        while j < N and S[i] == S[j]:
            j += 1
        ans += (j - i) * (j - i - 1) // 2
        i = j
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    S = [input() for _ in range(N)]

    # 1. 文字列をソート
    # 2. ソート後の文字列をキーにして、値には文字列のリストを持つ辞書を作成
    # 3. 辞書の値のリストの長さから組み合わせを計算
    # 4. 重複組み合わせを考慮して、組み合わせを計算
    # 5. 組み合わせを出力
    print(sum([len(v) * (len(v) - 1) // 2 for v in sorted([sorted(S)], key=lambda x: x[0])]))

=======
Suggestion 8

def main():
    #N個の文字列s_1, s_2, ... s_Nが与えられる
    #s_iは10文字の英小文字
    #s_iは全て異なる
    #i<jなるi,jのペアがあって、s_iがs_jのアナグラムであるとき、そのペアの個数を出力せよ
    #アナグラムとは、文字を並び替えてできた新しい文字列
    #例えば、greenbinはbeginnerのアナグラム
    #同じ文字が複数含まれている場合、その文字をその数だけ使わないといけない
    #例えば、greenbinはbeginnerのアナグラムではない
    #Nは2以上10^5以下
    #s_iは10文字の英小文字
    #s_1, s_2, ... s_Nは全て異なる
    #アナグラムのペアの個数を出力せよ
    N = int(input())
    s_list = [input() for _ in range(N)]
    #s_listの文字列をソートしたリストを作成する
    s_list_sorted = [''.join(sorted(s)) for s in s_list]
    #s_list_sortedの文字列をキーとして、出現回数を値とする辞書を作成する
    s_dict = {}
    for s in s_list_sorted:
        if s in s_dict:
            s_dict[s] += 1
        else:
            s_dict[s] = 1
    #s_dictの値を全て足し合わせる
    #値が2以上のとき、その値を2つ選ぶ組み合わせの個数を足し合わせる
    #例えば、s_dictの値が2, 4, 6のとき、
    #2つ選ぶ組み合わせは2C2=1通り、
