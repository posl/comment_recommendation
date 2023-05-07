def main():    
    N, M, Q = map(int, input().split())
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    X = [0] * M
    X = list(map(int, input().split()))
    for i in range(Q):
        L, R = map(int, input().split())
        X_tmp = X[:L-1] + X[R:]
        X_tmp.sort()
        W_tmp = W[:]
        V_tmp = V[:]
        ans = 0
        for j in range(len(X_tmp)):
            max_idx = -1
            max_value = -1
            for k in range(len(W_tmp)):
                if W_tmp[k] <= X_tmp[j]:
                    if V_tmp[k] > max_value:
                        max_value = V_tmp[k]
                        max_idx = k
            if max_idx != -1:
                ans += V_tmp[max_idx]
                W_tmp.pop(max_idx)
                V_tmp.pop(max_idx)
        print(ans)

if __name__ == '__main__':
    main()