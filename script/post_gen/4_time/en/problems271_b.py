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
        print(a[s - 1][t - 1])

=======
Suggestion 2

def main():
    n, q = map(int, input().split())
    seq = []
    for i in range(n):
        seq.append(list(map(int, input().split())))
    queries = []
    for i in range(q):
        queries.append(list(map(int, input().split())))
    for query in queries:
        print(seq[query[0]-1][query[1]-1])

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    seq = []
    for i in range(N):
        seq.append(list(map(int, input().split())))
    for i in range(Q):
        s, t = map(int, input().split())
        print(seq[s-1][t-1])

=======
Suggestion 4

def main():
    n, q = map(int, input().split())
    L = []
    for i in range(n):
        L.append(list(map(int, input().split())))
    for i in range(q):
        s, t = map(int, input().split())
        print(L[s-1][t-1])

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    seqs = []
    for i in range(N):
        seqs.append(list(map(int, input().split())))
    for i in range(Q):
        s, t = map(int, input().split())
        print(seqs[s-1][t-1])

=======
Suggestion 6

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
        s.append(int(input()))
        t.append(int(input()))
    return n, q, l, a, s, t

=======
Suggestion 7

def main():
    N,Q = map(int,input().split())
    L = []
    A = []
    for i in range(N):
        L.append(list(map(int,input().split())))
        A.append(list(map(int,input().split())))

    for i in range(Q):
        print(L[A[i][0]-1][A[i][1]-1])

=======
Suggestion 8

def main():
    # Get input
    N, Q = map(int, input().split())
    L = []
    A = []
    for i in range(N):
        l, *a = map(int, input().split())
        L.append(l)
        A.append(a)
    ST = []
    for i in range(Q):
        s, t = map(int, input().split())
        ST.append((s, t))
    # Solve
    for s, t in ST:
        print(A[s-1][t-1])
    return

=======
Suggestion 9

def get_answer(n, q, l, a, s, t):
    for i in range(q):
        print(a[s[i]-1][t[i]-1])
