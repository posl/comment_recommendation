def solve():
    N,M,Q = map(int,input().split())
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i],V[i] = map(int,input().split())
    X = [0] * M
    X = list(map(int,input().split()))
    query = [0] * Q
    for i in range(Q):
        query[i] = list(map(int,input().split()))
    for i in range(Q):
        L = query[i][0]
        R = query[i][1]
        X1 = X[:L-1]
        X2 = X[R:]
        X1.extend(X2)
        X1.sort()
        X2 = X1
        X2 = X2[::-1]
        X1 = X1[::-1]
        X3 = X1[:N]
        X4 = X2[:N]
        ans = 0
        for j in range(1<<N):
            w = 0
            v = 0
            for k in range(N):
                if j & (1<<k):
                    w += W[k]
                    v += V[k]
            if w > X3[0]:
                continue
            if w <= X4[0]:
                ans = max(ans,v)
                continue
            l = 0
            r = N-1
            while r-l > 1:
                m = (l+r)//2
                if w <= X4[m]:
                    l = m
                else:
                    r = m
            ans = max(ans,v+X4[l+1]-w)
        print(ans)
solve()
