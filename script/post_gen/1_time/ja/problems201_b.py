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
    T2 = sorted(T, reverse=True)
    for i in range(N):
        if T[i] == T2[1]:
            print(S[i])
            return

=======
Suggestion 2

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S_i, T_i = input().split()
        S.append(S_i)
        T.append(int(T_i))
    T_max = max(T)
    T.remove(T_max)
    T_max2 = max(T)
    print(S[T.index(T_max2)])

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
    max1 = max(T)
    T.remove(max1)
    max2 = max(T)
    print(S[T.index(max2)])

=======
Suggestion 4

def main():
    n = int(input())
    mountain = []
    for i in range(n):
        s, t = input().split()
        mountain.append([s, int(t)])
    mountain.sort(key=lambda x: x[1], reverse=True)
    print(mountain[1][0])

=======
Suggestion 5

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S_i, T_i = input().split()
        S.append(S_i)
        T.append(int(T_i))
    T.sort(reverse=True)
    print(S[T.index(T[1])])

=======
Suggestion 6

def main():
    N = int(input())
    d = {}
    for i in range(N):
        S, T = input().split()
        d[S] = int(T)
    d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    print(d[1][0])

=======
Suggestion 7

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    T.sort()
    ans = S[T.index(T[N-2])]
    print(ans)

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
    S = [x for _, x in sorted(zip(T, S), reverse=True)]
    print(S[1])

=======
Suggestion 9

def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s.append(input().split())
    for i in range(n):
        t.append(int(s[i][1]))
    t.sort(reverse=True)
    print(s[t.index(t[1])][0])

=======
Suggestion 10

def main():
    N = int(input())
    mountain = []
    for i in range(N):
        mountain.append(input().split())
    mountain.sort(key=lambda x: int(x[1]), reverse=True) #高さでソート
    print(mountain[1][0])
