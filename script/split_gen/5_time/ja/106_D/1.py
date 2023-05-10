def solve():
    N,M,Q = map(int,input().split())
    LR = [list(map(int,input().split())) for _ in range(M)]
    PQ = [list(map(int,input().split())) for _ in range(Q)]
    LR.sort(key=lambda x:x[1])
    for p,q in PQ:
        ans = 0
        for l,r in LR:
            if p<=l and r<=q:
                ans += 1
        print(ans)
