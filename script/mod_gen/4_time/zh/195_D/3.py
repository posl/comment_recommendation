def solve():
    N,M,Q=map(int,input().split())
    W=[]
    V=[]
    for _ in range(N):
        w,v=map(int,input().split())
        W.append(w)
        V.append(v)
    X=list(map(int,input().split()))
    Query=[]
    for _ in range(Q):
        l,r=map(int,input().split())
        Query.append((l-1,r-1))
    ans=[]
    for l,r in Query:
        box=X[:l]+X[r+1:]
        box.sort()
        dp=[0]*(M+1)
        for i in range(N):
            w,v=W[i],V[i]
            for j in range(M-1,-1,-1):
                if box[j]>=w:
                    dp[j+1]=max(dp[j+1],dp[j]+v)
        ans.append(max(dp))
    print('\n'.join(map(str,ans)))
solve()
