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
