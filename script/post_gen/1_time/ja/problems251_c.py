Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = [0] * N
    T = [0] * N
    for i in range(N):
        S[i], T[i] = input().split()
        T[i] = int(T[i])
    #print(N, S, T)

    # 1. S と T を対応付けた辞書を作る
    # 2. S と T を対応付けた辞書を S でソートする
    # 3. S と T を対応付けた辞書を T でソートする
    # 4. T でソートした辞書の中で最も後ろにあるものを最優秀賞とする

    # 1. S と T を対応付けた辞書を作る
    ST = {}
    for i in range(N):
        ST[S[i]] = T[i]

    # 2. S と T を対応付けた辞書を S でソートする
    ST_sort_S = sorted(ST.items(), key=lambda x:x[0])
    #print(ST_sort_S)

    # 3. S と T を対応付けた辞書を T でソートする
    ST_sort_T = sorted(ST.items(), key=lambda x:x[1], reverse=True)
    #print(ST_sort_T)

    # 4. T でソートした辞書の中で最も後ろにあるものを最優秀賞とする
    #print(ST_sort_T[0][0])
    #print(ST_sort_S)
    for i in range(N):
        if ST_sort_T[0][0] == ST_sort_S[i][0]:
            print(i+1)
            break

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
    ans = 0
    for i in range(N):
        if S[i] in S[:i]:
            continue
        if ans == 0:
            ans = i
        elif T[i] > T[ans]:
            ans = i
    print(ans+1)

=======
Suggestion 3

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    ans = 0
    max = 0
    for i in range(N):
        for j in range(i):
            if S[i] == S[j]:
                break
        else:
            if T[i] > max:
                ans = i + 1
                max = T[i]
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    d = {}
    for i in range(n):
        s, t = input().split()
        t = int(t)
        if s not in d:
            d[s] = [t, i]
        else:
            if d[s][0] < t:
                d[s] = [t, i]
    d = sorted(d.items(), key=lambda x: x[1][1])
    print(d[0][1][1] + 1)

=======
Suggestion 5

def main():
    N = int(input())
    D = {}
    for i in range(N):
        S, T = input().split()
        T = int(T)
        if S in D:
            D[S] = max(D[S], T)
        else:
            D[S] = T

    T = []
    for s, t in D.items():
        T.append((t, s))

    T.sort(reverse=True)

    for i in range(N):
        S, T = input().split()
        T = int(T)
        if (T, S) == T[0]:
            print(i+1)
            break

=======
Suggestion 6

def main():
    N = int(input())
    d = {}
    for i in range(N):
        s, t = input().split()
        t = int(t)
        if s not in d:
            d[s] = [t, i]
        else:
            if d[s][0] < t:
                d[s] = [t, i]
    ans = 10**5
    for i in d.values():
        ans = min(ans, i[1])
    print(ans+1)

=======
Suggestion 7

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S_i, T_i = input().split()
        S.append(S_i)
        T.append(int(T_i))

    # 重複を削除したSを作成
    S_set = list(set(S))
    # 重複を削除したSの要素数を取得
    S_set_len = len(S_set)

    # 重複を削除したSの要素数分だけループ
    for i in range(S_set_len):
        # 重複を削除したSの要素を取得
        S_set_i = S_set[i]
        # 同じ要素のインデックスを取得
        S_set_i_index = [j for j, x in enumerate(S) if x == S_set_i]
        # 同じ要素のインデックスの要素数を取得
        S_set_i_index_len = len(S_set_i_index)
        # 同じ要素のインデックスの要素数が1の場合は最優秀賞
        if S_set_i_index_len == 1:
            # 最優秀賞のインデックスを取得
            best_index = S_set_i_index[0]
            # 最優秀賞のインデックス+1を出力
            print(best_index+1)
            break
        # 同じ要素のインデックスの要素数が1より大きい場合は最優秀賞を探す
        else:
            # 同じ要素のインデックスの要素数分だけループ
            for j in range(S_set_i_index_len):
                # 同じ要素のインデックスを取得
                S_set_i_index_j = S_set_i_index[j]
                # 同じ要素のインデックスの要素数分だけループ
                for k in range(S_set_i_index_len):
                    # 同じ要素のインデックスを取得
                    S_set_i_index_k

=======
Suggestion 8

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    max_point = -1
    max_point_index = -1
    for i in range(N):
        if T[i] > max_point:
            max_point = T[i]
            max_point_index = i
    max_point_count = 0
    for i in range(N):
        if T[i] == max_point:
            max_point_count += 1
    if max_point_count == 1:
        print(max_point_index+1)
        return
    for i in range(N):
        if T[i] == max_point:
            for j in range(i):
                if S[i] == S[j]:
                    max_point_count -= 1
                    break
    if max_point_count == 1:
        for i in range(N):
            if T[i] == max_point:
                for j in range(i):
                    if S[i] == S[j]:
                        print(j+1)
                        return
    else:
        for i in range(N):
            if T[i] == max_point:
                print(i+1)
                return

=======
Suggestion 9

def main():
    N = int(input())
    S = []
    T = []
    for _ in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))

    # まずは最も得点が高い提出を探す
    max_score = max(T)
    max_score_index = T.index(max_score)

    # 最も得点が高い提出の文字列を取得
    max_score_string = S[max_score_index]

    # 最も得点が高い提出よりも早い提出で、最も得点が高い提出と文字列が一致する提出を探す
    for i in range(max_score_index):
        if T[i] == max_score and S[i] == max_score_string:
            max_score_index = i

    print(max_score_index + 1)
