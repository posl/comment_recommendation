def main():
    N, M, Q = map(int, input().split())
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    X = [0] * M
    for i in range(M):
        X[i] = int(input())
    for i in range(Q):
        L, R = map(int, input().split())
        W_ = W.copy()
        V_ = V.copy()
        X_ = X.copy()
        for j in range(L - 1, R):
            X_[j] = 0
        ans = 0
        for j in range(M):
            if X_[j] == 0:
                continue
            max_ = 0
            for k in range(N):
                if W_[k] <= X_[j] and V_[k] > max_:
                    max_ = V_[k]
                    max_k = k
            ans += max_
            W_[max_k] = 0
            V_[max_k] = 0
        print(ans)
