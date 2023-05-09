def main():
    N, M, Q = map(int, input().split())
    W = []
    V = []
    for i in range(N):
        w, v = map(int, input().split())
        W.append(w)
        V.append(v)
    X = list(map(int, input().split()))
    L = []
    R = []
    for i in range(Q):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    for i in range(Q):
        X_ = X[:L[i]-1] + X[R[i]:]
        X_.sort()
        ans = 0
        for j in range(N):
            for k in range(M-1, -1, -1):
                if W[j] <= X_[k]:
                    ans += V[j]
                    X_.pop(k)
                    break
        print(ans)
    return
main()
