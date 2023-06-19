Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, q = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))

    for i in range(q):
        s, t = map(int, input().split())
        print(a[s-1][t-1])

=======
Suggestion 2

def main():
    n, q = map(int, input().split())
    a = []
    for i in range(n):
        tmp = list(map(int, input().split()))
        a.append(tmp[1:])
    for i in range(q):
        s, t = map(int, input().split())
        print(a[s-1][t-1])

=======
Suggestion 3

def main():
    n,q = map(int,input().split())
    L = []
    for i in range(n):
        L.append(list(map(int,input().split())))
    S = []
    for i in range(q):
        S.append(list(map(int,input().split())))
    for i in range(q):
        print(L[S[i][0]-1][S[i][1]-1])

=======
Suggestion 4

def read_ints():
    return list(map(int, input().split()))

=======
Suggestion 5

def get_input():
    n, q = input().split()
    n = int(n)
    q = int(q)
    seq = []
    for i in range(n):
        seq.append(input().split())
    query = []
    for i in range(q):
        query.append(input().split())
    return n, q, seq, query

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    seq = []
    for i in range(N):
        seq.append(list(map(int, input().split())))
    for i in range(Q):
        s, t = map(int, input().split())
        print(seq[s-1][t-1])

=======
Suggestion 7

def main():
    n, q = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split()))[1:])
    for i in range(q):
        s, t = map(int, input().split())
        print(a[s-1][t-1])
