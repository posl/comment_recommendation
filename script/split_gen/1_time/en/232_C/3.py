def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(M)]
    B = [list(map(int, input().split())) for _ in range(M)]
    for i in range(M):
        A[i][0] -= 1
        A[i][1] -= 1
        B[i][0] -= 1
        B[i][1] -= 1
    for p in range(N):
        for q in range(N):
            for r in range(N):
                for s in range(N):
                    for t in range(N):
                        for u in range(N):
                            for v in range(N):
                                for w in range(N):
                                    P = [p, q, r, s, t, u, v, w]
                                    flag = True
                                    for i in range(M):
                                        if (A[i][0] in P and A[i][1] in P) != (B[i][P.index(A[i][0])] in P and B[i][P.index(A[i][1])] in P):
                                            flag = False
                                            break
                                    if flag:
                                        print('Yes')
                                        return
    print('No')
    return
