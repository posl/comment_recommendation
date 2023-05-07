def main():
    N, M, Q = map(int, input().split())
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    X = list(map(int, input().split()))
    for i in range(Q):
        L, R = map(int, input().split())
        X1 = X[:L-1] + X[R:]
        X1.sort()
        V1 = [0] * N
        for j in range(N):
            for k in range(len(X1)):
                if X1[k] >= W[j]:
                    V1[j] = V[j]
                    X1[k] = 0
                    break
        print(sum(V1))

if __name__ == '__main__':
    main()