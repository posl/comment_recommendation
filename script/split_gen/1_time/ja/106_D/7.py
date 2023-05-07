def main():
    N,M,Q = map(int,input().split())
    LR = [list(map(int,input().split())) for _ in range(M)]
    PQ = [list(map(int,input().split())) for _ in range(Q)]
    LR.sort()
    PQ.sort()
    LR = [[l,r] for l,r in LR]
    PQ = [[p,q] for p,q in PQ]
    #print(LR)
    #print(PQ)
    for p,q in PQ:
        count = 0
        for l,r in LR:
            if p <= l and r <= q:
                count += 1
        print(count)
