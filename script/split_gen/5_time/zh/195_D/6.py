def main():
    N, M, Q = map(int, input().split())
    W = []
    V = []
    for i in range(N):
        w, v = map(int, input().split())
        W.append(w)
        V.append(v)
    X = list(map(int, input().split()))
    query = []
    for i in range(Q):
        l, r = map(int, input().split())
        query.append([l, r])
    for i in range(Q):
        l, r = query[i]
        X_copy = X.copy()
        del X_copy[l-1:r]
        X_copy.sort()
        W_copy = W.copy()
        V_copy = V.copy()
        ans = 0
        for j in range(N):
            for k in range(M-len(X_copy)):
                if W_copy[j] <= X_copy[k]:
                    ans += V_copy[j]
                    del W_copy[j]
                    del V_copy[j]
                    break
        print(ans)
