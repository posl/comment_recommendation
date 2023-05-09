Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    L = []
    A = []
    for i in range(N):
        l, *a = map(int, input().split())
        L.append(l)
        A.append(a)
    for i in range(Q):
        s, t = map(int, input().split())
        print(A[s-1][t-1])

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    seq = []
    for i in range(N):
        seq.append(list(map(int, input().split())))
    queries = []
    for i in range(Q):
        queries.append(list(map(int, input().split())))
    for i in range(Q):
        print(seq[queries[i][0]-1][queries[i][1]-1])

=======
Suggestion 3

def main():
    n, q = map(int, input().split())
    sequences = []
    for _ in range(n):
        sequences.append(list(map(int, input().split())))
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().split())))
    for query in queries:
        print(sequences[query[0]-1][query[1]-1])

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))

    for _ in range(Q):
        s, t = map(int, input().split())
        print(A[s-1][t-1])

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    for i in range(Q):
        s, t = map(int, input().split())
        print(L[s - 1][t - 1])

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    S = []
    T = []
    for i in range(Q):
        s, t = map(int, input().split())
        S.append(s)
        T.append(t)
    for i in range(Q):
        print(L[S[i] - 1][T[i] - 1])

=======
Suggestion 7

def main():
    n, q = map(int, input().split())
    seq = []
    for i in range(n):
        seq.append(list(map(int, input().split())))
    query = []
    for j in range(q):
        query.append(list(map(int, input().split())))
    for k in range(q):
        print(seq[query[k][0]-1][query[k][1]-1])

=======
Suggestion 8

def main():
    N, Q = map(int, input().split())
    a = []
    for i in range(N):
        a.append(list(map(int, input().split()))[1:])
    for i in range(Q):
        s, t = map(int, input().split())
        print(a[s-1][t-1])

=======
Suggestion 9

def main():
    N, Q = map(int, input().split())
    #print(N, Q)
    L = []
    a = []
    for i in range(N):
        L.append(list(map(int, input().split())))
        a.append(list(map(int, input().split())))
    #print(L)
    #print(a)
    for i in range(Q):
        s, t = map(int, input().split())
        print(L[s-1][t-1])

=======
Suggestion 10

def main():
    N, Q = map(int, input().split())

    # 2次元配列を作成
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))

    # クエリを処理
    for i in range(Q):
        s, t = map(int, input().split())
        print(A[s-1][t-1])
