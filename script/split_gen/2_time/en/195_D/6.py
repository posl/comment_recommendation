def main():
    N, M, Q = map(int, input().split())
    W = []
    V = []
    for i in range(N):
        w, v = map(int, input().split())
        W.append(w)
        V.append(v)
    X = list(map(int, input().split()))
    for i in range(Q):
        L, R = map(int, input().split())
        x = X[:L-1] + X[R:]
        x.sort()
        v = [0] * N
        for j in range(N):
            for k in range(M):
                if W[j] <= x[k]:
                    v[j] = V[j]
                    x[k] = 0
                    break
        print(sum(v))
