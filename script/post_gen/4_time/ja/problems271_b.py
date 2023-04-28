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
        a.append(list(map(int, input().split())))
    b = []
    for i in range(q):
        b.append(list(map(int, input().split())))
    for i in range(q):
        print(a[b[i][0]-1][b[i][1]-1])

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))

    for i in range(Q):
        s, t = map(int, input().split())
        print(A[s-1][t-1])

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    S = []
    for i in range(Q):
        S.append(list(map(int, input().split())))
    for i in range(Q):
        print(A[S[i][0]-1][S[i][1]-1])

=======
Suggestion 5

def main():
    # ここにコード
    N, Q = map(int, input().split())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))

    for i in range(Q):
        s, t = map(int, input().split())
        print(L[s-1][t-1])

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())

    #数列を格納する配列
    a_list = []
    for i in range(N):
        a_list.append(list(map(int, input().split())))

    #クエリを格納する配列
    query_list = []
    for i in range(Q):
        query_list.append(list(map(int, input().split())))

    for i in range(Q):
        print(a_list[query_list[i][0]-1][query_list[i][1]-1])
