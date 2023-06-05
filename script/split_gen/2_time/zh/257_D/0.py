def solve(n,s,w):
    w.sort()
    ans = 0
    for i in range(n):
        if s[i]=='0':
            ans+=1
    minw = 10**9+1
    for i in range(n):
        if s[i]=='0':
            if w[i]<minw:
                minw = w[i]
    if minw==10**9+1:
        minw = 0
    maxw = -1
    for i in range(n):
        if s[i]=='1':
            if w[i]>maxw:
                maxw = w[i]
    if maxw==-1:
        maxw = 0
    if ans==0:
        return 0
    return min(ans,2*n-ans)
