Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = [0]*N
    T = [0]*N
    for i in range(N):
        S[i], T[i] = input().split()
        T[i] = int(T[i])
    S_set = set(S)
    S_set = sorted(S_set)
    S_set_num = len(S_set)
    S_set_index = [0]*S_set_num
    S_set_score = [0]*S_set_num
    S_set_score[0] = T[0]
    for i in range(1, N):
        if S[i] == S[i-1]:
            S_set_score[S_set_index[i-1]] = max(S_set_score[S_set_index[i-1]], T[i])
        else:
            S_set_index[i] = S_set_index[i-1] + 1
            S_set_score[S_set_index[i]] = T[i]
    max_score = max(S_set_score)
    for i in range(S_set_num):
        if S_set_score[i] == max_score:
            print(S.index(S_set[i])+1)
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
        if T[i] > T[ans]:
            ans = i
    print(ans + 1)

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
    max_score = 0
    for i in range(N):
        if S[i] not in S[:i]:
            if T[i] > max_score:
                max_score = T[i]
                ans = i + 1

    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    #print(S)
    #print(T)
    count = 0
    max = 0
    for i in range(N):
        if T[i] > max:
            count = i + 1
            max = T[i]
    print(count)

=======
Suggestion 5

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        s = s.strip()
        t = int(t)
        S.append(s)
        T.append(t)
    ans = 0
    for i in range(N):
        flag = 0
        for j in range(i):
            if S[i] == S[j]:
                flag = 1
                break
        if flag == 0:
            ans = i
    print(ans + 1)

=======
Suggestion 6

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))

    #print(S)
    #print(T)

    #print(S)
    #print(T)

    #最も得点が高い提出を求める
    S_T = []
    for i in range(N):
        S_T.append([S[i], T[i]])
    #print(S_T)

    #得点が高い順にソート
    S_T.sort(key = lambda x:x[1], reverse = True)
    #print(S_T)

    #print(S_T)

    #ソート後のリストを作成
    S_sort = []
    T_sort = []
    for i in range(N):
        S_sort.append(S_T[i][0])
        T_sort.append(S_T[i][1])
    #print(S_sort)
    #print(T_sort)

    #print(S_sort)
    #print(T_sort)

    #ソート後のリストから最も得点が高い提出を求める
    S_T_sort = []
    for i in range(N):
        S_T_sort.append([S_sort[i], T_sort[i]])
    #print(S_T_sort)

    #print(S_T_sort)

    #最も得点が高い提出を求める
    max_T = T_sort[0]
    #print(max_T)

    #最も得点が高い提出のインデックスを求める
    max_T_index = T.index(max_T)
    #print(max_T_index)

    #最も得点が高い提出のインデックスをもとに元のリストから最も得点が高い提出の文字列を求める
    max_S = S[max_T_index]
    #print(max_S)

    #最も得点が高い提出の文字列をもとに元のリストから最も得点が高い提出のインデックスを求める
    max_S_index = S.index(max_S)
    #print(max_S_index)

    #最も得点が高い提出のインデックスをもとに元のリストから最

=======
Suggestion 7

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s,t = input().split()
        S.append(s)
        T.append(int(t))
    ans = 0
    for i in range(N):
        flag = 0
        for j in range(i):
            if S[i] == S[j]:
                flag = 1
                break
        if flag == 0:
            if ans == 0:
                ans = i+1
            else:
                if T[ans-1] < T[i]:
                    ans = i+1
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S_i, T_i = input().split()
        S.append(S_i)
        T.append(int(T_i))

    #print(S)
    #print(T)
    max_score = 0
    max_score_count = 0
    for i in range(N):
        if T[i] > max_score:
            max_score = T[i]
            max_score_count = 1
        elif T[i] == max_score:
            max_score_count += 1

    if max_score_count == 1:
        print(T.index(max_score) + 1)
    else:
        for i in range(N):
            if T[i] == max_score:
                for j in range(i):
                    if S[i] == S[j]:
                        max_score_count -= 1
                        break
        if max_score_count == 1:
            for i in range(N):
                if T[i] == max_score:
                    print(i + 1)
                    break
        else:
            for i in range(N):
                if T[i] == max_score:
                    for j in range(i):
                        if S[i] == S[j]:
                            print(j + 1)
                            break
                    break

=======
Suggestion 9

def main():
    n = int(input())
    s = []
    t = []
    for _ in range(n):
        st = input().split()
        s.append(st[0])
        t.append(int(st[1]))
    ans = 0
    for i in range(n):
        if s[:i].count(s[i]) == 0:
            if ans == 0:
                ans = i
            elif t[ans] < t[i]:
                ans = i
    print(ans+1)

=======
Suggestion 10

def main():
    n = int(input())
    a = [input().split() for _ in range(n)]
    b = []
    for i in range(n):
        if a[i][0] not in b:
            b.append(a[i][0])
    c = []
    for i in range(n):
        if a[i][0] in b:
            c.append(a[i])
    d = []
    for i in range(len(c)):
        d.append(c[i][1])
    e = []
    for i in range(len(c)):
        e.append(int(c[i][1]))
    f = []
    for i in range(len(c)):
        if e[i] == max(e):
            f.append(i)
    print(f[0] + 1)
