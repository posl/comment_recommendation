def main():
    N, M, Q = map(int, input().split())
    W = []
    V = []
    X = []
    for _ in range(N):
        w, v = map(int, input().split())
        W.append(w)
        V.append(v)
    for _ in range(M):
        x = int(input())
        X.append(x)
    for _ in range(Q):
        L, R = map(int, input().split())
        X_ = X[:L-1] + X[R:]
        X_.sort()
        X_.reverse()
        W_ = W[:]
        V_ = V[:]
        ans = 0
        for x in X_:
            w_max = 0
            v_max = 0
            for i in range(len(W_)):
                if W_[i] <= x:
                    if v_max < V_[i]:
                        w_max = W_[i]
                        v_max = V_[i]
                        index = i
            if v_max != 0:
                W_.pop(index)
                V_.pop(index)
                ans += v_max
        print(ans)
