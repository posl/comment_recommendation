def main():
    N, M, Q = map(int, input().split())
    W = [0] * N
    V = [0] * N
    X = [0] * M
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    for i in range(M):
        X[i] = int(input())
    for i in range(Q):
        L, R = map(int, input().split())
        used = [False] * M
        for j in range(L-1, R):
            used[j] = True
        box = []
        for j in range(M):
            if not used[j]:
                box.append(X[j])
        box.sort()
        w = W.copy()
        v = V.copy()
        for j in range(len(box)):
            for k in range(N):
                if w[k] <= box[j]:
                    w[k] = 0
                    v[k] = 0
        print(sum(v))

if __name__ == '__main__':
    main()