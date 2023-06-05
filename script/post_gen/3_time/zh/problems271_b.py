Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def get_input():
    n,q = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    s = []
    t = []
    for i in range(q):
        s_,t_ = map(int, input().split())
        s.append(s_)
        t.append(t_)
    return n,q,a,s,t

=======
Suggestion 2

def solve():
    n, q = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))

    for i in range(q):
        s, t = map(int, input().split())
        print(a[s - 1][t - 1])

=======
Suggestion 3

def main():
    n, q = map(int, input().split())
    seq = []
    for i in range(n):
        seq.append(list(map(int, input().split())))
    for i in range(q):
        s, t = map(int, input().split())
        print(seq[s-1][t-1])
    return 0

=======
Suggestion 4

def get_input():
    n, q = map(int, input().split())
    l = []
    a = []
    for i in range(n):
        l.append(list(map(int, input().split())))
        a.append(list(map(int, input().split())))
    s = []
    t = []
    for i in range(q):
        s_t = list(map(int, input().split()))
        s.append(s_t[0])
        t.append(s_t[1])
    return n, q, l, a, s, t

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    ST = []
    for i in range(Q):
        ST.append(list(map(int, input().split())))

    for i in range(Q):
        print(L[ST[i][0]-1][ST[i][1]-1])

=======
Suggestion 6

def main():
    n,q = list(map(int,input().split()))
    a = []
    for i in range(n):
        a.append(list(map(int,input().split())))
    s = []
    for i in range(q):
        s.append(list(map(int,input().split())))
    for i in range(q):
        print(a[s[i][0]-1][s[i][1]-1])

=======
Suggestion 7

def main():
    n,q = map(int,input().split())
    a = []
    for i in range(n):
        a.append(list(map(int,input().split())))
    for i in range(q):
        s,t = map(int,input().split())
        print(a[s-1][t-1])

=======
Suggestion 8

def main():
    n, q = map(int, input().split())
    seq = []
    for i in range(n):
        seq.append(list(map(int, input().split()))[1:])
    for i in range(q):
        s, t = map(int, input().split())
        print(seq[s-1][t-1])

main()

=======
Suggestion 9

def main():
    N,Q = map(int,input().split())
    L = []
    A = []
    for i in range(N):
        l = list(map(int,input().split()))
        L.append(l[0])
        A.append(l[1:])
    S = []
    T = []
    for i in range(Q):
        s,t = map(int,input().split())
        S.append(s)
        T.append(t)
    for i in range(Q):
        print(A[S[i]-1][T[i]-1])
