Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    ts = []
    for i in range(N):
        s, t = input().split()
        t = int(t)
        ts.append((s, t, i + 1))
    ts.sort()
    max_s = None
    max_t = 0
    ans = 0
    for t in ts:
        if t[0] != max_s:
            max_s = t[0]
            max_t = t[1]
            ans = t[2]
        else:
            if t[1] > max_t:
                max_t = t[1]
                ans = t[2]
    print(ans)

=======
Suggestion 2

def solve(n, s, t):
    dic = {}
    for i in range(n):
        if s[i] not in dic:
            dic[s[i]] = [t[i], i]
        else:
            if t[i] > dic[s[i]][0]:
                dic[s[i]] = [t[i], i]
    max = 0
    for key in dic:
        if dic[key][0] > max:
            max = dic[key][0]
            index = dic[key][1]
    return index

n = int(input())
s = []
t = []
for i in range(n):
    temp = input().split()
    s.append(temp[0])
    t.append(int(temp[1]))
print(solve(n, s, t))

=======
Suggestion 3

def get_best_score():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))

    # print(S)
    # print(T)

    best_score = 0
    best_score_index = 0
    for i in range(N):
        if T[i] > best_score:
            best_score = T[i]
            best_score_index = i
    # print(best_score_index)

    best_score_string = S[best_score_index]
    # print(best_score_string)

    best_score_index = 0
    for i in range(N):
        if S[i] == best_score_string:
            if T[i] == best_score:
                best_score_index = i
                break
    # print(best_score_index)

    print(best_score_index + 1)

=======
Suggestion 4

def bestPoem():
    n=int(input())
    poem={}
    for i in range(n):
        s,t=input().split()
        if s in poem:
            if poem[s][0]<int(t):
                poem[s]=[int(t),i+1]
        else:
            poem[s]=[int(t),i+1]
    best=0
    bestPoem=''
    for i in poem:
        if poem[i][0]>best:
            best=poem[i][0]
            bestPoem=i
    return poem[bestPoem][1]

=======
Suggestion 5

def problems251_c():
    n = int(input())
    score = {}
    for i in range(n):
        s, t = input().split()
        if s not in score:
            score[s] = int(t)
        else:
            score[s] = max(score[s], int(t))
    max_score = max(score.values())
    for i in range(n):
        if score[s] == max_score:
            print(i + 1)
            break

=======
Suggestion 6

def judge_max_score(score_list):
    max_score = 0
    max_index = 0
    for index, score in enumerate(score_list):
        if score > max_score:
            max_score = score
            max_index = index
    return max_index

=======
Suggestion 7

def main():
    n = int(input())
    st = {}
    for i in range(n):
        s,t = input().split()
        t = int(t)
        if s in st:
            if st[s][0] < t:
                st[s] = [t,i]
        else:
            st[s] = [t,i]
    #print(st)
    max = 0
    for k in st:
        if st[k][0] > max:
            max = st[k][0]
            max_i = st[k][1]
    print(max_i+1)

=======
Suggestion 8

def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        l = input().split()
        s.append(l[0])
        t.append(int(l[1]))
    max_t = max(t)
    max_s = []
    for i in range(n):
        if t[i] == max_t:
            max_s.append(s[i])
    min_s = max_s[0]
    for i in range(len(max_s)):
        if min_s > max_s[i]:
            min_s = max_s[i]
    print(s.index(min_s)+1)

=======
Suggestion 9

def best_score(n, s, t):
    max_score = {}
    for i in range(n):
        if s[i] not in max_score:
            max_score[s[i]] = t[i]
        else:
            if max_score[s[i]] < t[i]:
                max_score[s[i]] = t[i]
    max_score = sorted(max_score.items(), key=lambda x: x[1], reverse=True)
    for i in range(len(max_score)):
        if max_score[i][1] == max_score[0][1]:
            return s.index(max_score[i][0]) + 1

=======
Suggestion 10

def problems251_c():
    n = int(input())
    best = 0
    best_score = 0
    best_time = 10**10
    for i in range(n):
        s,t = input().split()
        t = int(t)
        if t > best_score:
            best_score = t
            best = i
            best_time = 10**10
        elif t == best_score:
            if s == s:
                best = i
                best_time = 10**10
            else:
                best_time = min(best_time,i)
    print(best+1)
