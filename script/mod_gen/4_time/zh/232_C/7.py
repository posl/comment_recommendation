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
    for i in range(2 ** N):
        P = []
        for j in range(N):
            if (i >> j) & 1:
                P.append(j + 1)
        if len(P) != N:
            continue
        flag = True
        for j in range(M):
            if ((A[j] in P) and (B[j] in P)) or ((not (A[j] in P)) and (not (B[j] in P))):
                if ((C[j] in P) and (D[j] in P)) or ((not (C[j] in P)) and (not (D[j] in P))):
                    continue
                else:
                    flag = False
                    break
            else:
                if ((C[j] in P) and (D[j] in P)) or ((not (C[j] in P)) and (not (D[j] in P))):
                    flag = False
                    break
                else:
                    continue
        if flag:
            print("Yes")
            return
    print("No")
    return

if __name__ == '__main__':
    solve()