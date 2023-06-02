Synthesizing 9/10 solutions

=======
Suggestion 1

def find_best_submission(n, submissions):
    best_score = 0
    best_index = 0
    best_submission = ''
    for i in range(n):
        submission = submissions[i][0]
        score = submissions[i][1]
        if score > best_score:
            best_score = score
            best_index = i
            best_submission = submission
        elif score == best_score:
            if submission < best_submission:
                best_score = score
                best_index = i
                best_submission = submission
    return best_index + 1

=======
Suggestion 2

def get_best_submission(N, S, T):
    best_score = -1
    best_submission = -1
    for i in range(N):
        if T[i] > best_score:
            best_score = T[i]
            best_submission = i
    best_submissions = []
    for i in range(N):
        if T[i] == best_score:
            best_submissions.append(i)
    best_submission = best_submissions[0]
    for i in range(len(best_submissions)):
        if S[best_submissions[i]] < S[best_submission]:
            best_submission = best_submissions[i]
    return best_submission + 1

N = int(input())
S = []
T = []
for i in range(N):
    s, t = input().split()
    S.append(s)
    T.append(int(t))
print(get_best_submission(N, S, T))

=======
Suggestion 3

def main():
    n = int(input())
    dict = {}
    for i in range(n):
        s, t = input().split()
        if s not in dict:
            dict[s] = [i+1, int(t)]
        else:
            if int(t) > dict[s][1]:
                dict[s] = [i+1, int(t)]
    max = 0
    for k, v in dict.items():
        if v[1] > max:
            max = v[1]
            ans = v[0]
    print(ans)

=======
Suggestion 4

def solve():
    N = int(input())
    data = []
    for i in range(N):
        s, t = input().split()
        data.append((s, int(t)))
    data.sort(key=lambda x: (x[0], -x[1]))
    max_t = 0
    max_i = 0
    for i in range(N):
        if data[i][1] > max_t:
            max_t = data[i][1]
            max_i = i
    print(max_i + 1)

=======
Suggestion 5

def main():
    n = int(input())
    s_t = {}
    for i in range(n):
        s, t = input().split()
        t = int(t)
        if s not in s_t:
            s_t[s] = t
        else:
            s_t[s] += t
    s_t = sorted(s_t.items(), key=lambda x: x[1], reverse=True)
    print(s_t[0][0])

=======
Suggestion 6

def get_best_submission(N, S_T):
    # N = int(input())
    # S_T = [input().split() for _ in range(N)]
    # S_T = [input().split() for _ in range(N)]
    # print(N)
    # print(S_T)
    # print(S_T[0][1])
    # print(S_T[0][0])
    # print(S_T[0][1])
    # print(S_T[1][0])
    # print(S_T[1][1])
    # print(S_T[2][0])
    # print(S_T[2][1])
    # print(S_T[3][0])
    # print(S_T[3][1])
    # print(S_T[4][0])
    # print(S_T[4][1])
    # print(S_T[5][0])
    # print(S_T[5][1])
    # print(S_T[6][0])
    # print(S_T[6][1])
    # print(S_T[7][0])
    # print(S_T[7][1])
    # print(S_T[8][0])
    # print(S_T[8][1])
    # print(S_T[9][0])
    # print(S_T[9][1])

    # N = 3
    # S_T = [['aaa', '10'], ['bbb', '20'], ['aaa', '30']]
    # N = 5
    # S_T = [['aaa', '9'], ['bbb', '10'], ['ccc', '10'], ['ddd', '10'], ['bbb', '11']]
    # N = 10
    # S_T = [['bb', '3'], ['ba', '1'], ['aa', '4'], ['bb', '1'], ['ba', '5'], ['aa', '9'], ['aa', '2'], ['ab', '6'], ['bb', '5'], ['ab', '3']]
    # N = 5
    # S_T = [['aaa', '10'], ['bbb', '20'], ['aaa', '30'], ['aaa', '40'], ['aaa', '50']]
    # N = 5
    # S_T = [['aaa', '10'], ['bbb', '20'], ['aaa', '30'], ['aaa', '40'], ['bbb', '50']]
    # N =

=======
Suggestion 7

def main():
    n = int(input())
    scores = {}
    for i in range(n):
        s, t = input().split()
        t = int(t)
        if s not in scores:
            scores[s] = [t, i]
        else:
            if scores[s][0] < t:
                scores[s] = [t, i]
    max_score = 0
    max_score_index = 0
    for key in scores:
        if scores[key][0] > max_score:
            max_score = scores[key][0]
            max_score_index = scores[key][1]
    print(max_score_index + 1)

=======
Suggestion 8

def main():
    n = input()
    d = {}
    for i in range(n):
        s, t = raw_input().split()
        if s in d:
            d[s].append((i, int(t)))
        else:
            d[s] = [(i, int(t))]
    for k in d:
        d[k].sort(key=lambda x: x[1], reverse=True)
    ans = 0
    for k in d:
        if len(d[k]) > 1 and d[k][0][1] == d[k][1][1]:
            continue
        if d[k][0][1] > d[k][1][1]:
            ans = max(ans, d[k][0][0])
    print ans + 1

=======
Suggestion 9

def problems251_c():
    n = int(input())
    s = []
    t = []
    for _ in range(n):
        ss,tt = input().split()
        s.append(ss)
        t.append(int(tt))
    m = {}
    for i in range(n):
        if s[i] not in m:
            m[s[i]] = t[i]
    max_num = -1
    max_index = -1
    for i in range(n):
        if s[i] in m and m[s[i]] > max_num:
            max_num = m[s[i]]
            max_index = i
    print(max_index+1)
