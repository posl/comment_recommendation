Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    for i in range(Q):
        s, t = map(int, input().split())
        print(L[s-1][t])

=======
Suggestion 2

def main():
    N, Q = list(map(int, input().split()))
    L = []
    A = []
    for i in range(N):
        l = list(map(int, input().split()))
        L.append(l[0])
        A.append(l[1:])
    S = []
    T = []
    for i in range(Q):
        s, t = list(map(int, input().split()))
        S.append(s)
        T.append(t)
    for i in range(Q):
        print(A[S[i]-1][T[i]-1])

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    s = []
    t = []
    for i in range(Q):
        s_i, t_i = map(int, input().split())
        s.append(s_i)
        t.append(t_i)
    for i in range(Q):
        print(L[s[i] - 1][t[i]])

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    for j in range(Q):
        s, t = map(int, input().split())
        print(L[s-1][t])

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))
    S = []
    T = []
    for _ in range(Q):
        s, t = map(int, input().split())
        S.append(s)
        T.append(t)
    for i in range(Q):
        print(A[S[i]-1][T[i]-1])

main()

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    A = [[] for _ in range(N)]
    for i in range(N):
        A[i] = list(map(int, input().split()))
        A[i].pop(0)
    for _ in range(Q):
        s, t = map(int, input().split())
        print(A[s-1][t-1])

=======
Suggestion 7

def main():
    #input
    N, Q = map(int, input().split())
    L = [0] * N
    A = [0] * N
    for i in range(N):
        A[i] = list(map(int, input().split()))
        L[i] = A[i][0]
    S = [0] * Q
    T = [0] * Q
    for i in range(Q):
        S[i], T[i] = map(int, input().split())
    
    #solve
    Ls = [0] * (N + 1)
    for i in range(N):
        Ls[i + 1] = Ls[i] + L[i]
    
    #output
    for i in range(Q):
        print(A[S[i] - 1][T[i] - Ls[S[i] - 1] + Ls[S[i] - 1 - 1] + 1])

=======
Suggestion 8

def main():
    import sys
    input = sys.stdin.readline

    N, Q = map(int, input().split())
    L = [0] * N
    A = []
    for i in range(N):
        L[i] = int(input())
        A.append(list(map(int, input().split())))
    S = [0] * Q
    T = [0] * Q
    for i in range(Q):
        S[i], T[i] = map(int, input().split())

    #print(N, Q)
    #print(L)
    #print(A)
    #print(S)
    #print(T)

    # L[i] = len(A[i])
    # A[i][j] = i-th sequence, j-th term

    # A[i] = [a_{i, 1}, a_{i, 2}, ..., a_{i, L[i]}]
    # A = [A[0], A[1], ..., A[N-1]]
    # A[i][j] = a_{i, j}

    # S[k] = s_k
    # T[k] = t_k
    # S = [S[0], S[1], ..., S[Q-1]]
    # T = [T[0], T[1], ..., T[Q-1]]

    # A[i][j] = i-th sequence, j-th term

    # A[i] = [a_{i, 1}, a_{i, 2}, ..., a_{i, L[i]}]
    # A = [A[0], A[1], ..., A[N-1]]
    # A[i][j] = a_{i, j}

    # S[k] = s_k
    # T[k] = t_k
    # S = [S[0], S[1], ..., S[Q-1]]
    # T = [T[0], T[1], ..., T[Q-1]]

    # A[i][j] = i-th sequence, j-th term

    # A[i] = [a_{i, 1}, a_{i, 2}, ..., a_{i, L[i]}]
    # A = [A[0], A[1], ..., A[N-1]]
    # A[i][j] = a_{i, j}

    # S[k] =

=======
Suggestion 9

def main():
    N, Q = map(int, input().split())
    #print(N, Q)
    A = []
    for i in range(N):
        L = list(map(int, input().split()))
        #print(L)
        A.append(L)
    #print(A)
    for i in range(Q):
        s, t = map(int, input().split())
        #print(s, t)
        print(A[s-1][t])

=======
Suggestion 10

def main():
    # get input
    N, Q = map(int, input().split())
    A = []
    for _ in range(N):
        L, *a = map(int, input().split())
        A.append(a)
    S = []
    T = []
    for _ in range(Q):
        s, t = map(int, input().split())
        S.append(s)
        T.append(t)
    # solve
    ans = []
    for s, t in zip(S, T):
        ans.append(A[s - 1][t - 1])
    # output
    for a in ans:
        print(a)
