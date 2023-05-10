def main():
    N, M, Q = map(int, input().split())
    LR = []
    for i in range(M):
        l, r = map(int, input().split())
        LR.append((l, r))
    PQ = []
    for i in range(Q):
        p, q = map(int, input().split())
        PQ.append((p, q))
    for i in range(Q):
        ans = 0
        for j in range(M):
            if LR[j][0] >= PQ[i][0] and LR[j][1] <= PQ[i][1]:
                ans += 1
        print(ans)
