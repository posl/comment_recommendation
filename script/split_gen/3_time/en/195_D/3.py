def main():
    N, M, Q = map(int, input().split())
    W = [0]*N
    V = [0]*N
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    X = [0]*M
    X = list(map(int, input().split()))
    for i in range(Q):
        L, R = map(int, input().split())
        X2 = X[:L-1] + X[R:]
        X2.sort()
        V2 = [0]*N
        for j in range(N):
            for k in range(len(X2)):
                if X2[k] >= W[j]:
                    V2[j] = V[j]
                    X2[k] = 0
                    break
        print(sum(V2))
