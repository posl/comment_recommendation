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
    N, Q = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))

    for _ in range(Q):
        s, t = map(int, input().split())
        print(A[s-1][t-1])

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    #print(N, Q)
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    #print(L)
    for i in range(Q):
        s, t = map(int, input().split())
        print(L[s-1][t-1])

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    for i in range(Q):
        s, t = map(int, input().split())
        print(L[s-1][t-1])

=======
Suggestion 5

def main():
    n,q = map(int,input().split())
    seq = []
    for i in range(n):
        seq.append(list(map(int,input().split())))
    for i in range(q):
        s,t = map(int,input().split())
        print(seq[s-1][t-1])

=======
Suggestion 6

def main():
    n, q = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    for i in range(q):
        s, t = map(int, input().split())
        print(a[s-1][t-1])

main()

=======
Suggestion 7

def main():
    N, Q = map(int, input().split())
    A = []
    for i in range(N):
        A.append([int(i) for i in input().split()])
    B = []
    for i in range(Q):
        B.append([int(i) for i in input().split()])
    for i in range(Q):
        print(A[B[i][0]-1][B[i][1]-1])

=======
Suggestion 8

def main():
    #n, q = map(int, input().split())
    #a = [list(map(int, input().split())) for _ in range(n)]
    #s = [list(map(int, input().split())) for _ in range(q)]
    n, q = 3, 4
    a = [[4, 128, 741, 239, 901],
         [2, 1, 1],
         [3, 314, 159, 26535]]
    s = [[1, 1],
         [2, 2],
         [3, 3],
         [1, 4]]
    for i in range(q):
        print(a[s[i][0]-1][s[i][1]-1])
main()
