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
        L -= 1
        R -= 1
        #print(N, M, Q)
        #print(W)
        #print(V)
        #print(X)
        #print(L, R)
        #print()
        W2 = W[:]
        V2 = V[:]
        X2 = X[:]
        del W2[L:R+1]
        del V2[L:R+1]
        del X2[L:R+1]
        #print(W2)
        #print(V2)
        #print(X2)
        #print()
        V2, W2 = zip(*sorted(zip(V2, W2), reverse=True))
        #print(W2)
        #print(V2)
        #print()
        ans = 0
        for i in range(len(X2)):
            for j in range(len(W2)):
                if W2[j] <= X2[i]:
                    ans += V2[j]
                    X2[i] = 0
                    W2[j] = 10**6 + 1
                    break
        print(ans)
main()

if __name__ == '__main__':
    main()