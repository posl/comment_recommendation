Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)

=======
Suggestion 2

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))

    max_score = 0
    max_score_index = 0
    for i in range(N):
        if T[i] > max_score:
            max_score = T[i]
            max_score_index = i

    print(max_score_index + 1)

=======
Suggestion 3

def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        _s, _t = input().split()
        s.append(_s)
        t.append(int(_t))

    # print(s)
    # print(t)

    # 1. オリジナルの提出を抽出
    # 2. 最高得点のオリジナル提出を抽出
    # 3. 最高得点のオリジナル提出の中で最も早い提出を抽出

    # 1. オリジナルの提出を抽出
    # 1-1. 最初の提出をオリジナル提出として追加
    # 1-2. 2回目以降の提出をオリジナル提出と比較する
    # 1-3. すでにオリジナル提出として追加済みの場合は、次の提出を比較する
    # 1-4. すでにオリジナル提出として追加済みでない場合は、オリジナル提出として追加する
    original = []
    for i in range(n):
        if i == 0:
            original.append([s[i], t[i]])
        else:
            is_original = True
            for j in range(len(original)):
                if s[i] == original[j][0]:
                    is_original = False
                    break
            if is_original:
                original.append([s[i], t[i]])

    # print(original)

    # 2. 最高得点のオリジナル提出を抽出
    # 2-1. オリジナル提出の中から最高得点を抽出
    # 2-2. 最高得点のオリジナル提出を抽出
    max_score = 0
    max_original = []
    for i in range(len(original)):
        if max_score < original[i][1]:
            max_score = original[i][1]
            max_original = []
            max

=======
Suggestion 4

def main():
    N = int(input())
    ST = []
    for i in range(N):
        s, t = input().split()
        ST.append([s, int(t)])
    ST.sort(key=lambda x: x[1], reverse=True)
    S = set()
    for i in range(N):
        S.add(ST[i][0])
    S = list(S)
    S.sort()
    T = []
    for i in range(len(S)):
        T.append([S[i], 0])
    for i in range(N):
        for j in range(len(S)):
            if ST[i][0] == T[j][0]:
                T[j][1] = max(T[j][1], ST[i][1])
                break
    for i in range(len(S)):
        if T[i][1] == 0:
            T[i][1] = 10 ** 9 + 1
    T.sort(key=lambda x: x[1], reverse=True)
    for i in range(len(S)):
        if T[0][1] == T[i][1]:
            print(i + 1)
            break

=======
Suggestion 5

def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        tmp = input().split()
        s.append(tmp[0])
        t.append(int(tmp[1]))
    #print(s)
    #print(t)
    maxt = max(t)
    #print(maxt)
    maxtindex = t.index(maxt)
    #print(maxtindex)
    maxs = s[maxtindex]
    #print(maxs)
    s.pop(maxtindex)
    t.pop(maxtindex)
    #print(s)
    #print(t)
    while maxs in s:
        maxsindex = s.index(maxs)
        s.pop(maxsindex)
        t.pop(maxsindex)
    #print(s)
    #print(t)
    print(t.index(max(t))+2)

=======
Suggestion 6

def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        a, b = input().split()
        s.append(a)
        t.append(int(b))
    #print(s)
    #print(t)
    #print("--------------")

    # オリジナルな提出のみに絞る
    # その中で最も得点が高い提出が最優秀賞
    # その中で最も提出が早いものを最優秀賞とする

    # オリジナルな提出のみに絞る
    original = []
    for i in range(n):
        if s.count(s[i]) == 1:
            original.append(i)
    #print(original)

    # その中で最も得点が高い提出が最優秀賞
    # その中で最も提出が早いものを最優秀賞とする
    max = 0
    for i in original:
        if t[i] > max:
            max = t[i]
            best = i
    #print(best)
    print(best+1)

=======
Suggestion 7

def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        si, ti = input().split()
        s.append(si)
        t.append(int(ti))

    max_t = max(t)
    max_t_index = t.index(max_t)
    s_max_t = s[max_t_index]
    s_max_t_index = s.index(s_max_t)

    s_max_t_list = []
    for i in range(n):
        if s[i] == s_max_t:
            s_max_t_list.append(i)

    if len(s_max_t_list) == 1:
        print(s_max_t_index + 1)
    else:
        print(min(s_max_t_list) + 1)

=======
Suggestion 8

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s,t = input().split()
        S.append(s)
        T.append(int(t))
    #print(S)
    #print(T)
    #print(T[0])
    #print(T[1])
    #print(S[0])
    #print(S[1])
    #print(T[0] > T[1])
    #print(S[0] == S[1])
    #print(T[0] > T[1] and S[0] == S[1])
    #print(T[1] > T[0] and S[1] == S[0])
    #print(T[0] > T[1] and S[0] == S[1] and T[0] > T[2] and S[0] == S[2])
    #print(T[1] > T[0] and S[1] == S[0] and T[1] > T[2] and S[1] == S[2])
    #print(T[2] > T[0] and S[2] == S[0] and T[2] > T[1] and S[2] == S[1])
    #print(T[0] > T[1] and S[0] == S[1] and T[0] > T[2] and S[0] == S[2] and T[0] > T[3] and S[0] == S[3])
    #print(T[1] > T[0] and S[1] == S[0] and T[1] > T[2] and S[1] == S[2] and T[1] > T[3] and S[1] == S[3])
    #print(T[2] > T[0] and S[2] == S[0] and T[2] > T[1] and S[2] == S[1] and T[2] > T[3] and S[2] == S[3])
    #print(T[3] > T[0] and S[3] == S[0] and T[3] > T[1] and S[3] == S[

=======
Suggestion 9

def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        a, b = input().split()
        s.append(a)
        t.append(int(b))
    original = []
    for i in range(len(s)):
        if s[i] not in s[:i]:
            original.append(i)
    max = 0
    maxindex = 0
    for i in original:
        if t[i] > max:
            max = t[i]
            maxindex = i
    print(maxindex + 1)

=======
Suggestion 10

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s,t = input().split()
        S.append(s)
        T.append(int(t))
    # print(N)
    # print(S)
    # print(T)
    # print()
    # print()
    # print()

    # 一番最初の提出の得点
    max_score = max(T)
    # print(max_score)

    # 一番最初の提出の得点のインデックス
    max_score_index = T.index(max_score)
    # print(max_score_index)

    # 一番最初の提出の文字列
    max_score_string = S[max_score_index]
    # print(max_score_string)

    # 一番最初の提出の文字列のインデックス
    max_score_string_index = S.index(max_score_string)
    # print(max_score_string_index)

    # 一番最初の提出の文字列の得点
    max_score_string_score = T[max_score_string_index]
    # print(max_score_string_score)

    # 一番最初の提出の文字列の得点のインデックス
    max_score_string_score_index = T.index(max_score_string_score)
    # print(max_score_string_score_index)

    # 一番最初の提出の文字列の得点のインデックスが一番最初の提出のインデックスと一致していたら、一番最初の提出が最優秀賞
    if max_score_string_score_index == max_score_index:
        print(max_score_string_score_index+1)
    # 一番最初の提出の文字列の得点のインデックスが一番最初の提出のインデックスと一致していなかったら、一番最初の提出が最優秀賞ではない
    else:
        print(max_score_string_score_index+1)
