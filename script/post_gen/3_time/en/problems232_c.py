Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    C = [0] * M
    D = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    for i in range(M):
        C[i], D[i] = map(int, input().split())

    for i in range(1,N+1):
        for j in range(1,N+1):
            if i == j:
                continue
            if (i in A and j in A) or (i in B and j in B):
                if (i in C and j in C) or (i in D and j in D):
                    continue
                else:
                    print("No")
                    return
            else:
                if (i in C and j in C) or (i in D and j in D):
                    print("No")
                    return
                else:
                    continue
    print("Yes")

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    C = []
    D = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for _ in range(M):
        c, d = map(int, input().split())
        C.append(c)
        D.append(d)
    for i in range(N):
        if i + 1 not in A and i + 1 not in B and i + 1 not in C and i + 1 not in D:
            print("Yes")
            return
    print("No")

=======
Suggestion 3

def solve():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(M)]

    AB.sort()
    CD.sort()

    for i in range(M):
        AB[i].sort()
        CD[i].sort()

    AB.sort()
    CD.sort()

    for i in range(M):
        if AB[i] != CD[i]:
            print("No")
            exit()

    print("Yes")

=======
Suggestion 4

def solve():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(M)]

    AB.sort()
    CD.sort()

    for i in range(M):
        AB[i].append(i)
        CD[i].append(i)

    AB.sort(key=lambda x: x[1])
    CD.sort(key=lambda x: x[1])

    if AB == CD:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = [tuple(map(int, input().split())) for _ in range(m)]
    c = [tuple(map(int, input().split())) for _ in range(m)]
    for i in range(2 ** n):
        p = []
        for j in range(n):
            if i >> j & 1:
                p.append(j + 1)
        if len(p) != n:
            continue
        for j in range(m):
            if (a[j][0] in p and a[j][1] in p) != (c[j][0] in p and c[j][1] in p):
                break
        else:
            print('Yes')
            return
    print('No')

main()

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = []
    b = []
    for i in range(m):
        a1, b1 = map(int, input().split())
        a.append(a1)
        b.append(b1)
    c = []
    d = []
    for i in range(m):
        c1, d1 = map(int, input().split())
        c.append(c1)
        d.append(d1)
    for i in range(n):
        for j in range(n):
            if a[i] == c[j] and b[i] == d[j]:
                a[i] = 0
                b[i] = 0
                c[j] = 0
                d[j] = 0
    if sum(a) == 0 and sum(b) == 0 and sum(c) == 0 and sum(d) == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    N,M = map(int,input().split())
    A = []
    for i in range(M):
        A.append(list(map(int,input().split())))
    C = []
    for i in range(M):
        C.append(list(map(int,input().split())))
    def check(A,C):
        for i in range(len(A)):
            if A[i] in C:
                pass
            else:
                return False
        return True
    for i in range(N):
        A1 = [A[j] for j in range(M) if A[j][0] == i+1]
        C1 = [C[j] for j in range(M) if C[j][0] == i+1]
        if check(A1,C1):
            pass
        else:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 8

def solve(N,M,AB,CD):
    AB.sort()
    CD.sort()
    if AB == CD:
        return "Yes"
    else:
        return "No"

=======
Suggestion 9

def check_same_shape(N, M, A, B, C, D):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if (i, j) in zip(A, B) and (i, j) not in zip(C, D):
                return False
            if (i, j) not in zip(A, B) and (i, j) in zip(C, D):
                return False
    return True

=======
Suggestion 10

def main():
    #n, m = map(int, input().split())
    #a = [int(input()) for _ in range(n)]
    #b = [int(input()) for _ in range(m)]
    #print(n, m, a, b)
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(m)]
    c = [list(map(int, input().split())) for _ in range(m)]
    print(n, m, a, c)
    #print(n, m, a, b)
    #print(n, m, a, b, c, d)
    #print(n, m, a, b, c, d, sep='\n')
