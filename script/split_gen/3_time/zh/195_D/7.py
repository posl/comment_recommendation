def solve(N, M, Q, W, V, X, Query):
    ans = []
    for i in range(Q):
        L = Query[i][0]
        R = Query[i][1]
        X2 = X[0:L-1] + X[R:]
        X2.sort(reverse=True)
        W2 = W.copy()
        V2 = V.copy()
        for j in range(L-1, R):
            W2.remove(W[j])
            V2.remove(V[j])
        W2.sort(reverse=True)
        V2.sort(reverse=True)
        #print(W2, V2, X2)
        #print(L, R)
        #print(X[L-1:R])
        #print(W[L-1:R])
        #print(V[L-1:R])
        #print(X2)
        #print(W2)
        #print(V2)
        ans.append(solve2(W2, V2, X2))
    return ans
