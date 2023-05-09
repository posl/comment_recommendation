def main():
    N, M, Q = map(int, input().split())
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    X = [0] * M
    for i in range(M):
        X[i] = int(input())
    Query = [[0] * 2 for i in range(Q)]
    for i in range(Q):
        Query[i][0], Query[i][1] = map(int, input().split())
    for i in range(Q):
        L = Query[i][0]
        R = Query[i][1]
        X_copy = X.copy()
        X_copy[L - 1:R] = [0] * (R - L + 1)
        X_copy = [x for x in X_copy if x != 0]
        X_copy.sort()
        V_copy = V.copy()
        W_copy = W.copy()
        for j in range(len(X_copy)):
            for k in range(len(W_copy)):
                if W_copy[k] <= X_copy[j]:
                    V_copy[j] += V_copy[k]
                    W_copy[k] = 0
        print(sum(V_copy))

if __name__ == '__main__':
    main()