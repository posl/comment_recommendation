def main():
    N, M, Q = map(int, input().split())
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    X = list(map(int, input().split()))
    Query = [0] * Q
    for i in range(Q):
        Query[i] = list(map(int, input().split()))
    for i in range(Q):
        L = Query[i][0]
        R = Query[i][1]
        X2 = []
        for j in range(L-1):
            X2.append(X[j])
        for j in range(R, M):
            X2.append(X[j])
        X2.sort()
        ans = 0
        for j in range(N):
            for k in range(len(X2)):
                if W[j] <= X2[k]:
                    ans += V[j]
                    X2.pop(k)
                    break
        print(ans)

if __name__ == '__main__':
    main()