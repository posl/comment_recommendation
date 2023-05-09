Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = [0] * n
    t = [0] * n
    for i in range(n):
        s[i], t[i] = input().split()
        t[i] = int(t[i])
    max_t = max(t)
    t2 = [0] * n
    for i in range(n):
        if t[i] == max_t:
            t2[i] = 1
    for i in range(n):
        if t2[i] == 1:
            print(i+1)
            break

=======
Suggestion 2

def main():
    n = int(input())
    d = {}
    for i in range(n):
        s, t = input().split()
        t = int(t)
        if s in d:
            d[s] = max(d[s], t)
        else:
            d[s] = t
    ans = sorted(d.items(), key=lambda x: x[1], reverse=True)[0]
    print(ans[0])

=======
Suggestion 3

def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s_i, t_i = input().split()
        s.append(s_i)
        t.append(int(t_i))

    d = {}
    for i in range(n):
        if s[i] not in d:
            d[s[i]] = t[i]
        else:
            if d[s[i]] < t[i]:
                d[s[i]] = t[i]

    max_t = 0
    for i in d:
        if d[i] > max_t:
            max_t = d[i]

    for i in range(n):
        if t[i] == max_t:
            print(i + 1)
            break

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

    best = max(T)
    best_i = T.index(best)
    print(S[best_i])

=======
Suggestion 5

def main():
    n = int(input())
    max_score = 0
    max_score_index = 0
    for i in range(n):
        s, t = input().split()
        t = int(t)
        if t > max_score:
            max_score = t
            max_score_index = i + 1
    print(max_score_index)

=======
Suggestion 6

def main():
    n = int(input())
    st = []
    for i in range(n):
        s,t = input().split()
        st.append((s,int(t)))
    st.sort(key=lambda x: x[0])
    st.sort(key=lambda x: x[1], reverse=True)
    print(st[0][0])

=======
Suggestion 7

def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s1, t1 = input().split()
        s.append(s1)
        t.append(int(t1))
    best = 0
    for i in range(n):
        if t[i] > t[best]:
            best = i
    print(best + 1)

=======
Suggestion 8

def solve():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        ss, tt = input().split()
        s.append(ss)
        t.append(int(tt))
    for i in range(n):
        if s[i] == s[i+1]:
            t[i+1] = t[i]
    print(t.index(max(t))+1)

=======
Suggestion 9

def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        st = input().split()
        s.append(st[0])
        t.append(int(st[1]))
    s_t = sorted(zip(s,t), key=lambda x:x[1], reverse=True)
    s_t = sorted(s_t, key=lambda x:x[0])
    print(t.index(s_t[0][1])+1)

=======
Suggestion 10

def get_best_submission(submissions):
    submissions.sort(key=lambda x: x[1], reverse=True)
    return submissions[0][0]
