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
    ans = "No"
    for i in range(2**N):
        P = []
        for j in range(N):
            if ((i >> j) & 1):
                P.append(1)
            else:
                P.append(0)
        for j in range(N):
            if P[j] == 0:
                continue
            for k in range(N):
                if P[k] == 0:
                    continue
                if j == k:
                    continue
                if (j+1 in A and k+1 in B) or (j+1 in B and k+1 in A):
                    continue
                else:
                    P[j] = 0
                    P[k] = 0
                    break
        for j in range(N):
            if P[j] == 0:
                continue
            for k in range(N):
                if P[k] == 0:
                    continue
                if j == k:
                    continue
                if (j+1 in C and k+1 in D) or (j+1 in D and k+1 in C):
                    continue
                else:
                    P[j] = 0
                    P[k] = 0
                    break
        if 1 not in P:
            ans = "Yes"
            break
    print(ans)

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
    for i in range(M):
        if (A[i] in C and B[i] in D) or (A[i] in D and B[i] in C):
            continue
        else:
            print("No")
            exit()
    print("Yes")

main()

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
    for i in range(1 << N):
        P = [0] * N
        for j in range(N):
            if (i >> j) & 1:
                P[j] = 1
        flag = True
        for j in range(M):
            if (P[A[j] - 1] ^ P[B[j] - 1]) != (P[C[j] - 1] ^ P[D[j] - 1]):
                flag = False
        if flag:
            print("Yes")
            return
    print("No")

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    C = []
    D = []
    for j in range(M):
        c, d = map(int, input().split())
        C.append(c)
        D.append(d)
    if N == 1:
        print("Yes")
        return
    for i in range(0, N):
        for j in range(0, N):
            if i != j:
                if A.count(i+1) == C.count(j+1) and B.count(i+1) == D.count(j+1):
                    continue
                else:
                    print("No")
                    return
    print("Yes")

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(m)]
    c = [list(map(int, input().split())) for i in range(m)]
    for i in range(m):
        a[i][0] -= 1
        c[i][0] -= 1
    ans = "No"
    for i in range(2**n):
        p = []
        for j in range(n):
            if (i >> j) & 1:
                p.append(j)
        if len(p) != n/2:
            continue
        flag = True
        for j in range(m):
            if (a[j][0] in p) ^ (a[j][1] in p):
                flag = False
            if (c[j][0] in p) ^ (c[j][1] in p):
                flag = False
        if flag:
            ans = "Yes"
            break
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    C = []
    D = []
    for m in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for m in range(M):
        c, d = map(int, input().split())
        C.append(c)
        D.append(d)

    for n in range(2**N):
        flag = True
        for m in range(M):
            if not (((n >> (A[m]-1)) & 1) == ((n >> (B[m]-1)) & 1)):
                flag = False
                break
        if flag:
            for m in range(M):
                if not (((n >> (C[m]-1)) & 1) == ((n >> (D[m]-1)) & 1)):
                    flag = False
                    break
        if flag:
            print("Yes")
            return
    print("No")

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    ab = []
    cd = []
    for i in range(m):
        ab.append(list(map(int,input().split())))
    for i in range(m):
        cd.append(list(map(int,input().split())))
    ab.sort()
    cd.sort()
    for i in range(m):
        if ab[i] != cd[i]:
            print("No")
            break
        if i == m-1:
            print("Yes")

=======
Suggestion 8

def solve():
    N,M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    C = [0] * M
    D = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    for i in range(M):
        C[i], D[i] = map(int, input().split())
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            for k in range(M):
                if (A[k] == i+1 and B[k] == j+1) and (C[k] != i+1 or D[k] != j+1):
                    return False
                if (A[k] != i+1 or B[k] != j+1) and (C[k] == i+1 and D[k] == j+1):
                    return False
    return True

=======
Suggestion 9

def main():
    n, m = map(int,input().split())
    a = []
    b = []
    c = []
    d = []
    for i in range(m):
        x, y = map(int,input().split())
        a.append(x)
        b.append(y)
    for i in range(m):
        x, y = map(int,input().split())
        c.append(x)
        d.append(y)
    for i in range(n):
        for j in range(n):
            if (i+1 in a and j+1 in b) and (i+1 not in c and j+1 not in d):
                print("No")
                exit()
            elif (i+1 not in a and j+1 not in b) and (i+1 in c and j+1 in d):
                print("No")
                exit()
    print("Yes")

=======
Suggestion 10

def get_input():
    N, M = map(int, raw_input().split())
    A = []
    B = []
    C = []
    D = []
    for i in range(M):
        a, b = map(int, raw_input().split())
        A.append(a)
        B.append(b)
    for i in range(M):
        c, d = map(int, raw_input().split())
        C.append(c)
        D.append(d)
    return N, M, A, B, C, D
