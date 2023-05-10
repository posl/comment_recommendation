def solve(N,D,LR):
    LR.sort()
    LR.append([10**9+1,10**9+1])
    #print(LR)
    ans = 0
    for i in range(N):
        l,r = LR[i]
        nl,nr = LR[i+1]
        #print(l,r,nl,nr)
        if l==r:
            continue
        if l+D<=r:
            continue
        if l+D<=nl:
            continue
        if l+D>nr:
            ans += 1
            continue
        if l+D<=nr:
            ans += 1
            LR[i+1][0] = l+D
            continue
    return ans
