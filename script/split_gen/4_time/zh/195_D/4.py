def solve():
    N,M,Q = map(int,input().split())
    W = []
    V = []
    for i in range(N):
        w,v = map(int,input().split())
        W.append(w)
        V.append(v)
    X = list(map(int,input().split()))
    Query = []
    for i in range(Q):
        l,r = map(int,input().split())
        Query.append([l,r])
    for i in range(Q):
        l = Query[i][0]
        r = Query[i][1]
        X_tmp = X[:l-1] + X[r:]
        X_tmp.sort()
        ans = 0
        for j in range(N):
            for k in range(len(X_tmp)):
                if W[j] <= X_tmp[k]:
                    ans += V[j]
                    X_tmp.pop(k)
                    break
        print(ans)
solve()
