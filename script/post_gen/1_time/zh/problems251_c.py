Synthesizing 10/10 solutions

=======
Suggestion 1

def get_best_submission(N, S, T):
    # 1. get the best score
    # 2. get the earliest best score
    # 3. get the index of the earliest best score
    best_score = 0
    best_score_index = 0
    best_score_time = 0
    for i in range(N):
        if T[i] > best_score:
            best_score = T[i]
            best_score_index = i
            best_score_time = S[i]
        elif T[i] == best_score:
            if S[i] < best_score_time:
                best_score_index = i
                best_score_time = S[i]
    return best_score_index + 1

=======
Suggestion 2

def judge_best_submission():
    n = int(input())
    s_list = []
    t_list = []
    for i in range(n):
        s, t = input().split(' ')
        s_list.append(s)
        t_list.append(int(t))
    max_t = max(t_list)
    best_s = ''
    for i in range(n):
        if t_list[i] == max_t:
            best_s = s_list[i]
            break
    for i in range(n):
        if s_list[i] == best_s:
            print(i + 1)
            break

=======
Suggestion 3

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
    max_score = 0
    ans = 0
    for k, v in d.items():
        if v[0] > max_score:
            max_score = v[0]
            ans = v[1]
    print(ans+1)

=======
Suggestion 4

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        T.append(int(t))
        S.append(s)
    max_t = max(T)
    max_s = []
    for i in range(N):
        if T[i] == max_t:
            max_s.append(S[i])
    if len(max_s) == 1:
        print(S.index(max_s[0])+1)
    else:
        min_i = N
        for i in range(len(max_s)):
            if S.index(max_s[i]) < min_i:
                min_i = S.index(max_s[i])
        print(min_i+1)

=======
Suggestion 5

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s,t = input().split()
        S.append(s)
        T.append(int(t))
    max = 0
    max_index = 0
    for i in range(N):
        if T[i] > max:
            max = T[i]
            max_index = i
    print(max_index+1)
    return

=======
Suggestion 6

def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        ss, tt = input().split()
        s.append(ss)
        t.append(int(tt))
    #print(s)
    #print(t)
    #print(s.index('aa'))
    #print(t[s.index('aa')])
    #print(max(t))
    #print(t.index(max(t)))
    #print(s[t.index(max(t))])
    #print(s.index(s[t.index(max(t))]))
    #print(s.index(s[t.index(max(t))])+1)
    #print(s.index(s[t.index(max(t))])+1)
    #print(s.index(s[t.index(max(t))]))
    #print(s.index(s[t.index(max(t))])+1)
    #print(s.index(s[t.index(max(t))]))
    #print(s.index(s[t.index(max(t))])+1)
    #print(s.index(s[t.index(max(t))]))
    #print(s.index(s[t.index(max(t))])+1)
    #print(s.index(s[t.index(max(t))]))
    #print(s.index(s[t.index(max(t))])+1)
    #print(s.index(s[t.index(max(t))]))
    #print(s.index(s[t.index(max(t))])+1)
    #print(s.index(s[t.index(max(t))]))
    #print(s.index(s[t.index(max(t))])+1)
    #print(s.index(s[t.index(max(t))]))
    #print(s.index(s[t.index(max(t))])+1)
    #print(s.index(s[t.index(max(t))]))
    #print(s.index(s[t.index(max(t))])+1)
    print(s.index(s[t.index(max(t))])+1)

=======
Suggestion 7

def solve():
    n = int(input())
    s_t = []
    for i in range(n):
        s, t = input().split()
        s_t.append((s, int(t), i + 1))
    s_t.sort(key=lambda x: (x[0], -x[1]))
    print(s_t[-1][2])

=======
Suggestion 8

def get_input():
    n = int(input())
    if n < 1 or n > 100000:
        raise Exception('N is out of range')
    data = []
    for i in range(n):
        line = input().strip().split(' ')
        if len(line) != 2:
            raise Exception('Input format error')
        data.append((line[0], int(line[1])))
    return data

=======
Suggestion 9

def main():
    n = int(input())
    scores = {}
    for i in range(n):
        s, t = input().split()
        t = int(t)
        if s not in scores:
            scores[s] = t
        else:
            scores[s] += t
    max_score = 0
    max_score_s = ""
    for s in scores:
        if scores[s] > max_score:
            max_score = scores[s]
            max_score_s = s
    print(max_score_s)

=======
Suggestion 10

def main():
    n = int(input())

    # 用于记录原始提交物的字典
    # key:字符串，value:最早提交的索引
    original_submissions = {}

    # 用于记录最佳提交物的字典
    # key:字符串，value:最早提交的索引
    best_submissions = {}

    for i in range(n):
        # 获取输入的字符串和分数
        s, t = input().split()
        t = int(t)

        # 如果是原始提交物，则记录
        if s not in original_submissions:
            original_submissions[s] = i

        # 如果是最佳提交物，则记录
        if s not in best_submissions or t > best_submissions[s][1]:
            best_submissions[s] = [i, t]

    # 获取最佳提交物的索引
    best_submission = min(best_submissions.items(), key=lambda x: (x[1][1], x[1][0]))

    # 输出最佳提交物的索引
    print(best_submission[1][0] + 1)
