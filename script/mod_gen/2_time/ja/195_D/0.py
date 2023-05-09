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
        X_new = X[:L-1] + X[R:]
        X_new.sort(reverse=True)
        W_new = W[:]
        V_new = V[:]
        ans = 0
        for j in range(len(X_new)):
            for k in range(len(W_new)):
                if W_new[k] <= X_new[j]:
                    ans += V_new[k]
                    W_new[k] = 10**6 + 1
                    break
        print(ans)

if __name__ == '__main__':
    main()