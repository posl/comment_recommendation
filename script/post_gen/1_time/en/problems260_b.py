Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = []
    for i in range(N):
        C.append(A[i]+B[i])
    D = sorted(range(len(C)), key=C.__getitem__, reverse=True)
    E = sorted(D[:X])
    F = sorted(list(set(D)-set(E))[:Y])
    G = sorted(list(set(list(set(D)-set(E)))-set(F))[:Z])
    H = sorted(list(set(list(set(list(set(D)-set(E)))-set(F)))-set(G)))
    for i in range(len(E)):
        print(E[i]+1)
    for i in range(len(F)):
        print(F[i]+1)
    for i in range(len(G)):
        print(G[i]+1)
    for i in range(len(H)):
        print(H[i]+1)

=======
Suggestion 2

def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    C = []
    for i in range(N):
        C.append([A[i] + B[i], A[i], B[i], i + 1])

    C.sort(key=lambda x: x[0], reverse=True)
    C = C[:X + Y + Z]

    C.sort(key=lambda x: x[3])

    for i in range(X + Y + Z):
        print(C[i][3])

=======
Suggestion 3

def problems260_b():
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = []
    for i in range(n):
        c.append([i, a[i] + b[i]])
    c.sort(key=lambda x: x[1], reverse=True)
    c.sort(key=lambda x: x[0])
    for i in range(x + y + z):
        print(c[i][0] + 1)

=======
Suggestion 4

def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    AB = [A[i] + B[i] for i in range(N)]
    AB_sorted = sorted(AB, reverse=True)
    A_sorted = sorted(A, reverse=True)
    B_sorted = sorted(B, reverse=True)
    AB_rank = [0] * N
    A_rank = [0] * N
    B_rank = [0] * N
    for i in range(N):
        AB_rank[i] = AB_sorted.index(AB[i]) + 1
        A_rank[i] = A_sorted.index(A[i]) + 1
        B_rank[i] = B_sorted.index(B[i]) + 1
    AB_rank_sorted = sorted(AB_rank)
    A_rank_sorted = sorted(A_rank)
    B_rank_sorted = sorted(B_rank)
    AB_rank_sorted = AB_rank_sorted[:X+Y+Z]
    A_rank_sorted = A_rank_sorted[:X]
    B_rank_sorted = B_rank_sorted[:Y]
    AB_rank_sorted.sort()
    A_rank_sorted.sort()
    B_rank_sorted.sort()
    AB_rank_sorted = [i-1 for i in AB_rank_sorted]
    A_rank_sorted = [i-1 for i in A_rank_sorted]
    B_rank_sorted = [i-1 for i in B_rank_sorted]
    AB_rank_sorted = set(AB_rank_sorted)
    A_rank_sorted = set(A_rank_sorted)
    B_rank_sorted = set(B_rank_sorted)
    AB_rank_sorted = list(AB_rank_sorted)
    A_rank_sorted = list(A_rank_sorted)
    B_rank_sorted = list(B_rank_sorted)
    AB_rank_sorted.sort()
    A_rank_sorted.sort()
    B_rank_sorted.sort()
    AB_rank_sorted = [i+1 for i in AB_rank_sorted]
    A_rank_sorted = [i+1 for i in A_rank_sorted]
    B_rank_sorted = [i+1 for i in B_rank_sorted]
    AB_rank_sorted = set(AB_rank_sorted)
    A_rank_sorted = set(A_rank_sorted)
    B_rank_sorted = set(B_rank_sorted)
    AB_rank_sorted = list(AB_rank_sorted)
    A_rank_sorted = list(A_rank_sorted)
    B_rank_sorted = list(B_rank_sorted)
    AB_rank_sorted.sort

=======
Suggestion 5

def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [i for i in range(1, N+1)]
    D = list(zip(A, B, C))
    D.sort(key=lambda x: x[0], reverse=True)
    D.sort(key=lambda x: x[1], reverse=True)
    D.sort(key=lambda x: x[0]+x[1], reverse=True)
    for i in range(X+Y+Z):
        print(D[i][2])

=======
Suggestion 6

def main():
    N,X,Y,Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    AB = []
    for i in range(N):
        AB.append([A[i], B[i], i+1])
    AB.sort(reverse=True)
    AB = AB[:X+Y+Z]

    AB.sort(key=lambda x: x[2])

    for i in range(X):
        print(AB[i][2])
    for i in range(X, X+Y):
        print(AB[i][2])
    for i in range(X+Y, X+Y+Z):
        print(AB[i][2])

=======
Suggestion 7

def main():
    N,X,Y,Z = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = []
    for i in range(N):
        C.append((A[i],B[i],i+1))
    C.sort(key=lambda x: x[0], reverse=True)
    C = C[:X]
    C.sort(key=lambda x: x[1], reverse=True)
    C = C[:X+Y]
    C.sort(key=lambda x: x[0]+x[1], reverse=True)
    C = C[:X+Y+Z]
    C.sort(key=lambda x: x[2])
    for i in range(X+Y+Z):
        print(C[i][2])

=======
Suggestion 8

def main():
    N,X,Y,Z = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = [0]*N
    for i in range(N):
        C[i] = A[i]+B[i]
    D = [0]*N
    for i in range(N):
        D[i] = (C[i],A[i],i+1)
    D.sort(reverse=True)
    E = [0]*N
    for i in range(N):
        E[i] = (D[i][1],B[D[i][2]-1],D[i][2])
    E.sort(reverse=True)
    F = [0]*N
    for i in range(N):
        F[i] = (E[i][0]+E[i][1],E[i][2])
    F.sort(reverse=True)
    for i in range(X+Y+Z):
        print(F[i][1])

=======
Suggestion 9

def main():
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ab = [(i, a[i], b[i]) for i in range(n)]
    ab.sort(key=lambda x: x[1], reverse=True)
    ab.sort(key=lambda x: x[2], reverse=True)
    ab.sort(key=lambda x: x[1]+x[2], reverse=True)
    for i in range(x+y+z):
        print(ab[i][0]+1)

=======
Suggestion 10

def main():
    N, X, Y, Z = map(int, input().split())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]

    #print(N, X, Y, Z)
    #print(A)
    #print(B)

    C = []
    for i in range(N):
        C.append([A[i], B[i], i+1])

    #print(C)

    C.sort(key=lambda x: x[2])
    C.sort(key=lambda x: x[1], reverse=True)
    C.sort(key=lambda x: x[0], reverse=True)

    #print(C)

    for i in range(X):
        print(C[i][2])

    for i in range(Y):
        print(C[i+X][2])

    for i in range(Z):
        print(C[i+X+Y][2])
