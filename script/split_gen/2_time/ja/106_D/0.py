def main():
    N, M, Q = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(M)]
    PQ = [list(map(int, input().split())) for _ in range(Q)]
    #print(N, M, Q)
    #print(LR)
    #print(PQ)
    #LRの要素を順に見ていく
    for i in range(Q):
        cnt = 0
        #print(PQ[i])
        for j in range(M):
            #print(LR[j])
            if PQ[i][0] <= LR[j][0] and LR[j][1] <= PQ[i][1]:
                cnt += 1
        print(cnt)
