def problem106_d():
    N, M, Q = map(int, input().split())
    LR = []
    for i in range(M):
        L, R = map(int, input().split())
        LR.append((L, R))
    PQ = []
    for i in range(Q):
        P, Q = map(int, input().split())
        PQ.append((P, Q))
    ans = [0] * Q
    for i in range(M):
        for j in range(Q):
            if LR[i][0] <= PQ[j][0] and LR[i][1] >= PQ[j][1]:
                ans[j] += 1
    for i in range(Q):
        print(ans[i])
problem106_d()
