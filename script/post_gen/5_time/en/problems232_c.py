Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    C = []
    D = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for i in range(M):
        c, d = map(int, input().split())
        C.append(c)
        D.append(d)
    if M == 0:
        print("Yes")
        return
    for i in range(M):
        for j in range(M):
            if A[i] == C[j] and B[i] == D[j]:
                A[i] = 0
                B[i] = 0
                C[j] = 0
                D[j] = 0
    if 0 in A:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    C = []
    D = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for i in range(M):
        c, d = map(int, input().split())
        C.append(c)
        D.append(d)

    if M == 0:
        print('Yes')
        exit()

    for i in range(1, N+1):
        for j in range(1, N+1):
            if i == j:
                continue
            else:
                tmp = 0
                for k in range(M):
                    if (A[k] == i and B[k] == j) or (A[k] == j and B[k] == i):
                        tmp += 1
                if tmp == 0:
                    print('No')
                    exit()
                else:
                    continue

    print('Yes')
    exit()

=======
Suggestion 3

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
    ans = "No"
    for i in range(2 ** N):
        P = []
        for j in range(N):
            if ((i >> j) & 1) == 1:
                P.append(j + 1)
        if len(P) != N:
            continue
        for j in range(M):
            if A[j] in P and B[j] in P:
                continue
            elif A[j] in P or B[j] in P:
                break
        else:
            for j in range(M):
                if C[j] in P and D[j] in P:
                    continue
                elif C[j] in P or D[j] in P:
                    break
            else:
                ans = "Yes"
                break
    print(ans)

=======
Suggestion 4

def solve():
    N, M = map(int, input().split())
    A = []
    B = []
    C = []
    D = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for i in range(M):
        c, d = map(int, input().split())
        C.append(c)
        D.append(d)
    for i in range(1, N+1):
        for j in range(1, N+1):
            if (i in A and j in B) or (i in B and j in A):
                if (i in C and j in D) or (i in D and j in C):
                    continue
                else:
                    print('No')
                    exit()
            else:
                if (i in C and j in D) or (i in D and j in C):
                    print('No')
                    exit()
                else:
                    continue
    print('Yes')

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = [0] * m
    b = [0] * m
    c = [0] * m
    d = [0] * m
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    for i in range(m):
        c[i], d[i] = map(int, input().split())
    for i in range(2**n):
        p = []
        for j in range(n):
            if (i >> j) & 1:
                p.append(j+1)
        if len(p) == n:
            break
    for i in range(m):
        if (a[i] in p) ^ (b[i] in p):
            print('No')
            exit()
        if (c[i] in p) ^ (d[i] in p):
            print('No')
            exit()
    print('Yes')

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(M)]
    cd = [list(map(int, input().split())) for _ in range(M)]

    for i in range(N):
        for j in range(N):
            if [i+1, j+1] in ab and [i+1, j+1] not in cd:
                print("No")
                exit()
            elif [i+1, j+1] in cd and [i+1, j+1] not in ab:
                print("No")
                exit()

    print("Yes")

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    a = []
    b = []
    c = []
    d = []
    for i in range(m):
        x,y = map(int,input().split())
        a.append(x)
        b.append(y)
    for i in range(m):
        x,y = map(int,input().split())
        c.append(x)
        d.append(y)
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i == j:
                continue
            else:
                if (i in a and j in b) and (i not in c and j not in d):
                    print('No')
                    exit()
                elif (i not in a and j not in b) and (i in c and j in d):
                    print('No')
                    exit()
    print('Yes')

=======
Suggestion 8

def main():
    N,M = map(int,input().split())
    A = [list(map(int,input().split())) for i in range(M)]
    C = [list(map(int,input().split())) for i in range(M)]
    for i in range(2**N):
        P = []
        for j in range(N):
            if (i >> j) & 1:
                P.append(j+1)
        if len(P) == N:
            flg = True
            for a,b in A:
                if not (a in P and b in P):
                    flg = False
            for c,d in C:
                if not (c in P and d in P):
                    flg = False
            if flg:
                print("Yes")
                return
    print("No")

=======
Suggestion 9

def solve(N, M, A, B, C, D):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if (i + 1, j + 1) in zip(A, B) and not (i + 1, j + 1) in zip(C, D):
                return False
            if not (i + 1, j + 1) in zip(A, B) and (i + 1, j + 1) in zip(C, D):
                return False
    return True

=======
Suggestion 10

def check_shape(N, M, Takahashi, Aoki):
    #print("Takahashi: ", Takahashi)
    #print("Aoki: ", Aoki)
    for i in range(N):
        for j in range(N):
            if Takahashi[i][j] != Aoki[i][j]:
                return False
    return True
