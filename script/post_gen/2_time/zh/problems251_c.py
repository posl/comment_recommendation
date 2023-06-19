Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # N = int(input())
    # S = []
    # T = []
    # for i in range(N):
    #     s, t = input().split()
    #     S.append(s)
    #     T.append(int(t))
    # print(S, T)
    # print(S.index(min(S)))
    # print(T[S.index(min(S))])
    # print(S.index(max(S)))
    # print(T[S.index(max(S))])
    # print(S.index(min(S))

=======
Suggestion 2

def main():
    n = int(input())
    dic = {}
    for i in range(n):
        s, t = input().split()
        t = int(t)
        if s in dic:
            if dic[s][0] < t:
                dic[s] = (t, i)
        else:
            dic[s] = (t, i)
    ans = sorted(dic.items(), key=lambda x: (-x[1][0], x[1][1]))
    print(ans[0][1][1] + 1)

=======
Suggestion 3

def main():
    n = int(input())
    dic = {}
    for i in range(n):
        s, t = input().split()
        t = int(t)
        if s in dic:
            dic[s].append((t, i))
        else:
            dic[s] = [(t, i)]

    for s in dic:
        dic[s].sort(reverse=True)

    max_score = 0
    max_score_idx = 0
    max_score_first_idx = n
    for s in dic:
        if dic[s][0][0] > max_score:
            max_score = dic[s][0][0]
            max_score_idx = dic[s][0][1]
            max_score_first_idx = dic[s][0][1]
        elif dic[s][0][0] == max_score and dic[s][0][1] < max_score_first_idx:
            max_score_first_idx = dic[s][0][1]
            max_score_idx = dic[s][0][1]

    print(max_score_idx + 1)

=======
Suggestion 4

def get_max_score_index( n, s, t ):
    max_score = 0
    max_score_index = 0
    for i in range( 0, n ):
        if t[i] > max_score:
            max_score = t[i]
            max_score_index = i
    return max_score_index

=======
Suggestion 5

def main():
    n = int(input())
    d = {}
    for i in range(n):
        s, t = input().split()
        if s not in d:
            d[s] = [int(t), i]
        elif d[s][0] < int(t):
            d[s] = [int(t), i]
    ans = sorted(d.items(), key=lambda x: x[1], reverse=True)
    print(ans[0][1][1] + 1)

=======
Suggestion 6

def find_best_submission(N, S, T):
    best = -1
    best_score = -1
    for i in range(0, N):
        if S[i] == best:
            continue
        if T[i] > best_score:
            best = S[i]
            best_score = T[i]
    return best

=======
Suggestion 7

def main():
    n = int(input())
    d = dict()
    for i in range(n):
        s, t = input().split()
        t = int(t)
        if s in d:
            d[s].append((t, i))
        else:
            d[s] = [(t, i)]
    for k in d.keys():
        d[k].sort()
    ans = -1
    max_t = 0
    for k in d.keys():
        if len(d[k]) >= 2:
            if d[k][-1][0] > max_t:
                max_t = d[k][-1][0]
                ans = d[k][-1][1]
        if d[k][0][0] > max_t:
            max_t = d[k][0][0]
            ans = d[k][0][1]
    print(ans + 1)

=======
Suggestion 8

def max_score_index(score_list):
    max_index = 0
    max_score = 0
    for i in range(len(score_list)):
        if score_list[i] > max_score:
            max_score = score_list[i]
            max_index = i
    return max_index

=======
Suggestion 9

def get_input():
    n = int(input())
    s_t_list = []
    for i in range(n):
        s_t_list.append(input().split())
    return n, s_t_list

=======
Suggestion 10

def problems251_c():

    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    # print(S)
    # print(T)

    # S = ['bb', 'ba', 'aa', 'bb', 'ba', 'aa', 'aa', 'ab', 'bb', 'ab']
    # T = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    # N = len(S)

    # 按照T的降序排序
    T_sort = sorted(T, reverse=True)
    # print(T_sort)

    # 按照T的降序排序后，如果有相同的T值，那么按照S的升序排序
    T_sort_S = []
    for i in range(len(T_sort)):
        T_sort_S.append([T_sort[i], S[T.index(T_sort[i])]])
    # print(T_sort_S)

    # 按照T的降序排序后，如果有相同的T值，那么按照S的升序排序后，再按照S的升序排序
    T_sort_S_S = sorted(T_sort_S, key=lambda x: x[1])
    # print(T_sort_S_S)

    # 按照T的降序排序后，如果有相同的T值，那么按照S的升序排序后，再按照S的升序排序后，再按照T的降序排序
    T_sort_S_S_T = sorted(T_sort_S_S, key=lambda x: x[0], reverse=True)
    # print(T_sort_S_S_T)

    # 按照T的降序排序后，如果有相同的T值，那么按照S的升序排序后，再按照S的升序排序后，再按照T的降序排序后，再按照T的升序排序
    T_sort_S_S_T_T = sorted(T_sort_S_S_T, key=lambda x: x[0])
