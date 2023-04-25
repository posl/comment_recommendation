Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    dic = {}
    for i in range(n):
        s, t = input().split()
        t = int(t)
        if s not in dic:
            dic[s] = t
        else:
            dic[s] = max(dic[s], t)
    print(n - len(dic))

=======
Suggestion 2

def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s_i, t_i = input().split()
        s.append(s_i)
        t.append(int(t_i))
    best = 0
    best_i = 0
    for i in range(n):
        if s[i] not in s[:i]:
            if t[i] > best:
                best = t[i]
                best_i = i
    print(best_i + 1)

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
    T_max = max(T)
    T_max_index = T.index(T_max)
    S_max = S[T_max_index]
    S_max_index = []
    for i in range(N):
        if S[i] == S_max:
            S_max_index.append(i)
    if len(S_max_index) == 1:
        print(S_max_index[0] + 1)
    else:
        T_max_index = []
        for i in range(len(S_max_index)):
            T_max_index.append(T.index(T[S_max_index[i]]))
        print(min(T_max_index) + 1)

=======
Suggestion 4

def main():
    n = int(input())
    s = []
    t = []
    for _ in range(n):
        a, b = input().split()
        s.append(a)
        t.append(int(b))
    ans = 0
    max_t = 0
    for i in range(n):
        if s[i] not in s[:i] and t[i] > max_t:
            ans = i + 1
            max_t = t[i]
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s_i, t_i = input().split()
        s.append(s_i)
        t.append(int(t_i))
    s_set = set(s)
    s_list = list(s_set)
    s_list.sort()
    s_dict = {}
    for i in range(len(s_list)):
        s_dict[s_list[i]] = i
    t_list = [0] * len(s_list)
    for i in range(n):
        t_list[s_dict[s[i]]] = max(t_list[s_dict[s[i]]], t[i])
    t_list.sort()
    print(t_list[-1])

=======
Suggestion 6

def main():
    N = int(input())
    scores = []
    for i in range(N):
        S, T = input().split()
        T = int(T)
        scores.append([i, S, T])
    scores.sort(key=lambda x: x[1])
    scores.sort(key=lambda x: x[2], reverse=True)
    for i in range(N):
        if scores[i][0] == 0:
            print(i + 1)
            break

=======
Suggestion 7

def solve():
    n = int(input())
    s = [input().split() for _ in range(n)]
    d = {}
    for i in range(n):
        if s[i][0] in d:
            d[s[i][0]] = max(d[s[i][0]], int(s[i][1]))
        else:
            d[s[i][0]] = int(s[i][1])
    ans = 0
    for i in range(n):
        if s[i][0] in d and d[s[i][0]] == int(s[i][1]):
            ans = i + 1
            break
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    a = [input().split() for i in range(n)]
    score = {}
    for i in range(n):
        if a[i][0] not in score:
            score[a[i][0]] = int(a[i][1])
        else:
            score[a[i][0]] = max(score[a[i][0]], int(a[i][1]))
    for i in range(n):
        if score[a[i][0]] == int(a[i][1]):
            print(i+1)
            exit()
main()

=======
Suggestion 9

def main():
    n = int(input())
    data = [input().split() for i in range(n)]
    data = [[s, int(t), i] for i, (s, t) in enumerate(data)]
    data.sort(key=lambda x: x[1], reverse=True)
    data.sort(key=lambda x: x[0])
    for i in range(1, n):
        if data[i - 1][0] == data[i][0]:
            data[i][1] = 0
    data.sort(key=lambda x: x[1], reverse=True)
    print(data[0][2] + 1)

=======
Suggestion 10

def main():
    n = int(input())
    scores = []
    for _ in range(n):
        s, t = input().split()
        scores.append((s, int(t)))
    best_score = 0
    best_score_index = 0
    for i, (s, t) in enumerate(scores):
        if t > best_score and s not in [s for s, _ in scores[:i]]:
            best_score = t
            best_score_index = i
    print(best_score_index + 1)
