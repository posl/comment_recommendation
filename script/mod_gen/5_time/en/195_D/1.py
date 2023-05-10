def main():
    N, M, Q = map(int, input().split())
    W = [0]*N
    V = [0]*N
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    X = list(map(int, input().split()))
    for i in range(Q):
        L, R = map(int, input().split())
        X_ = X[:L-1] + X[R:]
        X_.sort()
        ans = 0
        for j in range(N):
            for k in range(M-L-R+1):
                if W[j] <= X_[k]:
                    ans += V[j]
                    X_.pop(k)
                    break
        print(ans)

if __name__ == '__main__':
    main()