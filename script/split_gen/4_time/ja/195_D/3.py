def main():
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
        Query.append((l,r))
    for i in range(Q):
        l = Query[i][0]
        r = Query[i][1]
        X_copy = X.copy()
        X_copy.pop(l-1)
        X_copy.pop(r-1)
        X_copy.sort()
        ans = 0
        for j in range(N):
            for k in range(M-2):
                if W[j] <= X_copy[k]:
                    ans += V[j]
                    X_copy.pop(k)
                    break
        print(ans)
