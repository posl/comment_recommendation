Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = [None] * N
    T = [None] * N
    for i in range(N):
        S[i], T[i] = input().split()
        T[i] = int(T[i])
    print(N - max(T) + 1)

=======
Suggestion 2

def main():
    N = int(input())
    dic = {}
    for i in range(N):
        S, T = input().split()
        T = int(T)
        if S not in dic:
            dic[S] = T
        else:
            dic[S] = max(dic[S], T)
    max_val = max(dic.values())
    for i in range(N):
        S, T = input().split()
        T = int(T)
        if S in dic and dic[S] == max_val:
            print(i+1)
            break

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
    d = {}
    for i in range(N):
        if S[i] not in d:
            d[S[i]] = T[i]
        else:
            d[S[i]] = max(d[S[i]], T[i])
    for i in range(N):
        if T[i] == d[S[i]]:
            print(i+1)
            exit()

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
    best = 0
    for i in range(N):
        if S[i] not in S[:i] and T[i] > T[best]:
            best = i
    print(best + 1)

=======
Suggestion 5

def main():
    N = int(input())
    dic = {}
    for i in range(N):
        S,T = input().split()
        T = int(T)
        if S in dic:
            dic[S] = max(dic[S],T)
        else:
            dic[S] = T
    dic = sorted(dic.items(),key=lambda x:x[1],reverse=True)
    print(dic[0][1])

=======
Suggestion 6

def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        si, ti = input().split()
        s.append(si)
        t.append(int(ti))
    ans = 0
    for i in range(n):
        if s[i] not in s[:i]:
            if t[i] > t[ans]:
                ans = i
    print(ans + 1)

=======
Suggestion 7

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S.append(input().split()[0])
        T.append(int(input().split()[1]))
    for i in range(N):
        if S[i] in S[:i]:
            T[i] = -1
    print(T.index(max(T)))

=======
Suggestion 8

def main():
    N = int(input())
    dic = {}
    for i in range(N):
        s,t = input().split()
        t = int(t)
        if s in dic:
            if t > dic[s][0]:
                dic[s] = (t,i)
        else:
            dic[s] = (t,i)
    print(min(dic.values())[1]+1)

=======
Suggestion 9

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S.append(input().split()[0])
        T.append(int(input().split()[1]))
    maxT = max(T)
    for i in range(N):
        if T[i] == maxT:
            if S[i] not in S[:i]:
                print(i+1)
                break

=======
Suggestion 10

def main():
    n = int(input())
    t = 0
    s = []
    for i in range(n):
        s.append(input().split())
        s[i][1] = int(s[i][1])
    for i in range(n - 1):
        if s[i][0] == s[i + 1][0] and s[i][1] > s[i + 1][1]:
            t = s[i][1]
            s[i][1] = s[i + 1][1]
            s[i + 1][1] = t
    for i in range(n):
        if s[i][1] == s[n - 1][1]:
            print(i + 1)
            break
