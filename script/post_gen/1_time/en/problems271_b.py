Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    S = [list(map(int, input().split())) for _ in range(Q)]
    for s, t in S:
        print(A[s-1][t-1])

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    L = []
    A = []
    for i in range(N):
        tmp = list(map(int, input().split()))
        L.append(tmp[0])
        A.append(tmp[1:])
    S = []
    T = []
    for i in range(Q):
        s, t = map(int, input().split())
        S.append(s)
        T.append(t)
    for i in range(Q):
        print(A[S[i]-1][T[i]-1])

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))
    for _ in range(Q):
        s, t = map(int, input().split())
        print(A[s-1][t-1])

=======
Suggestion 4

def main():
    n, q = [int(x) for x in input().split()]
    a = []
    for i in range(n):
        a.append([int(x) for x in input().split()])
    for i in range(q):
        s, t = [int(x) for x in input().split()]
        print(a[s-1][t])

=======
Suggestion 5

def main():
    n, q = map(int, input().split())
    l = [0] * n
    a = []
    for i in range(n):
        l[i] = int(input().split()[0])
        a.append(list(map(int, input().split())))
    for i in range(q):
        s, t = map(int, input().split())
        print(a[s-1][t-1])

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    L = []
    A = []
    for i in range(N):
        L.append(list(map(int, input().split())))
        A.append(L[i][1:])
    S = []
    T = []
    for i in range(Q):
        S.append(int(input()))
        T.append(int(input()))
    for i in range(Q):
        print(A[S[i] - 1][T[i] - 1])

=======
Suggestion 7

def solve():
    N, Q = map(int, input().split())
    A = []
    for _ in range(N):
        L, *a = list(map(int, input().split()))
        A.append(a)
    for _ in range(Q):
        s, t = map(int, input().split())
        print(A[s-1][t-1])

solve()

=======
Suggestion 8

def main():
    N, Q = map(int, input().split())
    L = []
    L.append(0)
    for i in range(N):
        L.append(list(map(int, input().split())))
    for i in range(Q):
        s, t = map(int, input().split())
        print(L[s][t])

=======
Suggestion 9

def main():
    N, Q = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(N)]
    seq = [sum(L[i]) for i in range(N)]
    for i in range(1, N):
        seq[i] += seq[i - 1]
    for _ in range(Q):
        s, t = map(int, input().split())
        if s == 1:
            print(L[0][t - 1])
        else:
            print(L[s - 1][t - 1 - seq[s - 2]])

=======
Suggestion 10

def main():
    N, Q = map(int, input().split())
    len_seq = []
    seq = []
    for i in range(N):
        seq.append(list(map(int, input().split())))
        len_seq.append(seq[i].pop(0))
    for i in range(Q):
        s, t = map(int, input().split())
        print(seq[s-1][t-1])
