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
        X_tmp = X.copy()
        for j in range(L-1, R):
            X_tmp[j] = -1
        X_tmp.sort()
        W_tmp = W.copy()
        V_tmp = V.copy()
        for j in range(M):
            if X_tmp[j] == -1:
                continue
            for k in range(N):
                if W_tmp[k] > X_tmp[j]:
                    W_tmp[k] = -1
                    V_tmp[k] = -1
        W_tmp.sort()
        V_tmp.sort()
        ans = 0
        for j in range(N):
            if W_tmp[j] == -1:
                continue
            for k in range(N):
                if W_tmp[j] <= W[k] and V_tmp[N-1-k] != -1:
                    ans += V_tmp[N-1-k]
                    W_tmp[j] = -1
                    V_tmp[N-1-k] = -1
                    break
        print(ans)
