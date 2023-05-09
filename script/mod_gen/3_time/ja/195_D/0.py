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
        X2 = X[:L-1] + X[R:]
        X2.sort()
        W2 = W[:]
        V2 = V[:]
        ans = 0
        for j in range(len(X2)):
            for k in range(len(W2)):
                if W2[k] <= X2[j]:
                    W2[k] = 10**10
                    ans += V2[k]
                    break
        print(ans)

if __name__ == '__main__':
    main()