Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    d = {}
    for i in range(n):
        s, t = input().split()
        t = int(t)
        if s in d:
            d[s].append(t)
        else:
            d[s] = [t]
    for k, v in d.items():
        d[k] = sorted(v, reverse=True)
    # print(d)
    d = sorted(d.items(), key=lambda x: x[1][0], reverse=True)
    # print(d)
    print(d[0][1][1])

=======
Suggestion 2

def problems251_c():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s_t = input().split()
        s.append(s_t[0])
        t.append(int(s_t[1]))
    max_t = max(t)
    max_s = []
    for i in range(n):
        if t[i] == max_t:
            max_s.append(s[i])
    max_s.sort()
    print(s.index(max_s[0])+1)
    return

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

    #print(S)
    #print(T)

    best_score = 0
    best_index = 0
    for i in range(N):
        if T[i] > best_score:
            best_score = T[i]
            best_index = i

    print(best_index+1)

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

    max_score = 0
    best_submission = 0
    for i in range(N):
        if T[i] > max_score:
            max_score = T[i]
            best_submission = i

    print(best_submission + 1)

=======
Suggestion 5

def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        st = input().split()
        s.append(st[0])
        t.append(int(st[1]))
    #print(s)
    #print(t)
    maxt = max(t)
    #print(maxt)
    for i in range(n):
        if t[i] == maxt:
            print(s[i])
            break

=======
Suggestion 6

def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        st = input().split()
        s.append(st[0])
        t.append(int(st[1]))
    max = 0
    for i in range(n):
        if t[i] > max:
            max = t[i]
            max_s = s[i]
    print(s.index(max_s) + 1)

=======
Suggestion 7

def main():
    #N = int(input())
    #S = [input() for i in range(N)]
    #T = [int(input()) for i in range(N)]
    N = 10
    S = ['bb', 'ba', 'aa', 'bb', 'ba', 'aa', 'aa', 'ab', 'bb', 'ab']
    T = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    d = {}
    for i in range(N):
        if S[i] in d:
            d[S[i]].append((T[i], i))
        else:
            d[S[i]] = [(T[i], i)]
    #print(d)
    for k, v in d.items():
        d[k] = sorted(v, key=lambda x: x[0], reverse=True)
    #print(d)
    ans = sorted(d.items(), key=lambda x: x[1][0][0], reverse=True)[0][1][0][1]
    print(ans + 1)

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
    maxScore = max(T)
    maxScoreIndex = T.index(maxScore)
    print(S[maxScoreIndex])

=======
Suggestion 9

def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline

    N = int(input())
    S = defaultdict(lambda: 0)
    for i in range(N):
        s, t = input().split()
        S[s] = int(t)

    S = sorted(S.items(), key=lambda x: x[1], reverse=True)
    print(list(S)[0][0])

=======
Suggestion 10

def main():
    import sys
    import collections
    n = int(input())
    l = []
    for i in range(n):
        s, t = input().split()
        l.append([s, int(t)])
    d = collections.defaultdict(int)
    for i in range(n):
        s, t = l[i]
        d[s] += t
    m = max(d.values())
    for i in range(n):
        s, t = l[i]
        if d[s] == m:
            print(i+1)
            sys.exit()
    print('error')
