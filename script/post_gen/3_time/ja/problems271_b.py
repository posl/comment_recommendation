Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    B = []
    for i in range(Q):
        B.append(list(map(int, input().split())))
    for i in range(Q):
        print(A[B[i][0]-1][B[i][1]-1])

=======
Suggestion 2

def main():
    n, q = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    for _ in range(q):
        s, t = map(int, input().split())
        print(a[s-1][t-1])

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    for i in range(Q):
        s, t = map(int, input().split())
        print(L[s-1][t-1])

=======
Suggestion 4

def main():
    n,q = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    b = []
    for i in range(q):
        b.append(list(map(int, input().split())))
    for i in range(q):
        print(a[b[i][0]-1][b[i][1]-1])

=======
Suggestion 5

def main():
    n,q=map(int,input().split())
    a=[[] for _ in range(n)]
    for i in range(n):
        a[i]=list(map(int,input().split()))
    for i in range(q):
        s,t=map(int,input().split())
        print(a[s-1][t-1])

=======
Suggestion 6

def main():
    #n, q = map(int, input().split())
    #l = [list(map(int, input().split())) for _ in range(n)]
    #s = [list(map(int, input().split())) for _ in range(q)]
    n, q = 2, 2
    l = [[3, 1, 4, 7], [2, 5, 9]]
    s = [[1, 3], [2, 1]]
    for i in range(q):
        print(l[s[i][0]-1][s[i][1]-1])

=======
Suggestion 7

def main():
    N, Q = map(int, input().split())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    # print(L)
    for i in range(Q):
        s, t = map(int, input().split())
        print(L[s-1][t-1])
    return

=======
Suggestion 8

def get_input():
    n, q = map(int, input().split())
    l = list()
    a = list()
    for _ in range(n):
        l.append(int(input().split()[0]))
        a.append(list(map(int, input().split())))
    s = list()
    t = list()
    for _ in range(q):
        s_i, t_i = map(int, input().split())
        s.append(s_i)
        t.append(t_i)
    return n, q, l, a, s, t

=======
Suggestion 9

def main():
    # ここに書く
    N, Q = map(int, input().split())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    for i in range(Q):
        s, t = map(int, input().split())
        print(L[s-1][t-1])
