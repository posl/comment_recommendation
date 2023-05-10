def solve(N,D,LR):
    LR.sort()
    L,R = [],[]
    for l,r in LR:
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    L.append(10**9+1)
    R.append(10**9+1)
    ans = 0
    l,r = 0,0
    for i in range(1,N+1):
        while L[l] <= i:
            l += 1
        while R[r] <= i:
            r += 1
        ans = max(ans,r-l)
    return ans
N,D = map(int,input().split())
LR = [list(map(int,input().split())) for _ in range(N)]
print(solve(N,D,LR))
