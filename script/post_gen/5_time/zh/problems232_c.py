Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

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
    for i in range(1 << N):
        P = []
        for j in range(N):
            if (i >> j) & 1:
                P.append(j + 1)
        if len(P) != N:
            continue
        ok = True
        for j in range(M):
            if not ((A[j] in P and B[j] in P) or (A[j] not in P and B[j] not in P)):
                ok = False
                break
            if not ((C[j] in P and D[j] in P) or (C[j] not in P and D[j] not in P)):
                ok = False
                break
        if ok:
            ans = "Yes"
            break
    print(ans)

=======
Suggestion 3

def solve():
    n,m = map(int,input().split())
    a = []
    b = []
    c = []
    d = []
    for i in range(m):
        ai,bi = map(int,input().split())
        a.append(ai)
        b.append(bi)
    for i in range(m):
        ci,di = map(int,input().split())
        c.append(ci)
        d.append(di)
    for i in range(n):
        for j in range(n):
            if i != j:
                if (i+1 in a and j+1 in a) or (i+1 in b and j+1 in b):
                    if (i+1 in c and j+1 in c) or (i+1 in d and j+1 in d):
                        pass
                    else:
                        print('No')
                        return
                if (i+1 in c and j+1 in c) or (i+1 in d and j+1 in d):
                    if (i+1 in a and j+1 in a) or (i+1 in b and j+1 in b):
                        pass
                    else:
                        print('No')
                        return
    print('Yes')
    return

solve()

=======
Suggestion 4

def main():
    n,m = map(int,input().split())
    a = []
    b = []
    c = []
    d = []
    for i in range(m):
        a1,b1 = map(int,input().split())
        a.append(a1)
        b.append(b1)
    for i in range(m):
        c1,d1 = map(int,input().split())
        c.append(c1)
        d.append(d1)
    if a == c and b == d:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = []
    b = []
    c = []
    d = []
    for i in range(m):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    for i in range(m):
        c_i, d_i = map(int, input().split())
        c.append(c_i)
        d.append(d_i)
    aoki = []
    for i in range(n):
        aoki.append(i+1)
    high = []
    for i in range(n):
        high.append(i+1)
    for i in range(m):
        high[a[i]-1], high[b[i]-1] = high[b[i]-1], high[a[i]-1]
    for i in range(m):
        if aoki[c[i]-1] != high[c[i]-1] or aoki[d[i]-1] != high[d[i]-1]:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 6

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
    # print(A)
    # print(B)
    # print(C)
    # print(D)
    # print(N)
    # print(M)

    # #判断是否有相同的形状
    # #1.判断是否有相同的绳子
    # for i in range(M):
    #     for j in range(M):
    #         if A[i] == C[j] and B[i] == D[j]:
    #             print('Yes')
    #             return
    #         elif A[i] == D[j] and B[i] == C[j]:
    #             print('Yes')
    #             return
    # print('No')

    #2.判断是否有相同的绳子
    #1.判断是否有相同的绳子
    for i in range(M):
        for j in range(M):
            if A[i] == C[j] and B[i] == D[j]:
                print('Yes')
                return
            elif A[i] == D[j] and B[i] == C[j]:
                print('Yes')
                return
    print('No')

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    a, b = [], []
    for i in range(m):
        a0, b0 = map(int, input().split())
        a.append(a0)
        b.append(b0)
    c, d = [], []
    for i in range(m):
        c0, d0 = map(int, input().split())
        c.append(c0)
        d.append(d0)
    # print(a, b)
    # print(c, d)
    # print(n, m)
    # print(n, m)
    if n == 1:
        print('Yes')
    elif n == 2:
        if m == 0:
            print('Yes')
        elif m == 1:
            if a[0] == c[0] and b[0] == d[0]:
                print('Yes')
            else:
                print('No')
        else:
            print('No')
    elif n == 3:
        if m == 0:
            print('Yes')
        elif m == 1:
            if a[0] == c[0] and b[0] == d[0]:
                print('Yes')
            else:
                print('No')
        else:
            print('No')
    elif n == 4:
        if m == 0:
            print('Yes')
        elif m == 1:
            if a[0] == c[0] and b[0] == d[0]:
                print('Yes')
            else:
                print('No')
        elif m == 2:
            if a[0] == c[0] and b[0] == d[0] and a[1] == c[1] and b[1] == d[1]:
                print('Yes')
            else:
                print('No')
        elif m == 3:
            if a[0] == c[0] and b[0] == d[0] and a[1] == c[1] and b[1] == d[1] and a[2] == c[2] and b[2] == d[2]:
                print('Yes')
            else:
                print('No')
        elif m == 4:
            if a[0] == c[0] and b[0] == d[0]

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    a = []
    b = []
    c = []
    d = []
    for i in range(m):
        a1, b1 = map(int, input().split())
        a.append(a1)
        b.append(b1)
    for i in range(m):
        c1, d1 = map(int, input().split())
        c.append(c1)
        d.append(d1)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if (i + 1 in a and j + 1 in b) or (i + 1 in b and j + 1 in a):
                if not ((i + 1 in c and j + 1 in d) or (i + 1 in d and j + 1 in c)):
                    print('No')
                    return
            if (i + 1 in c and j + 1 in d) or (i + 1 in d and j + 1 in c):
                if not ((i + 1 in a and j + 1 in b) or (i + 1 in b and j + 1 in a)):
                    print('No')
                    return
    print('Yes')

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    a = []
    b = []
    c = []
    d = []
    for i in range(m):
        a1,b1 = map(int,input().split())
        a.append(a1)
        b.append(b1)
    for i in range(m):
        c1,d1 = map(int,input().split())
        c.append(c1)
        d.append(d1)
    if n == 1:
        print("Yes")
    else:
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                else:
                    if (i+1 in a) == (j+1 in c) and (i+1 in b) == (j+1 in d):
                        continue
                    else:
                        print("No")
                        return
        print("Yes")
