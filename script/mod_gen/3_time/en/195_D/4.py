def solve():
    N, M, Q = map(int, input().split())
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    X = [0] * M
    for i in range(M):
        X[i] = int(input())
    for q in range(Q):
        L, R = map(int, input().split())
        #L,R = map(int, input().split())
        #L -= 1
        #R -= 1
        #print(L, R)
        #print(X)
        #print(W)
        #print(V)
        #print(X)
        #print(X[:L-1])
        #print(X[R:])
        #print(X[:L-1] + X[R:])
        X2 = X[:L-1] + X[R:]
        #print(X2)
        X3 = sorted(X2, reverse=True)
        #print(X3)
        W2 = sorted(W, reverse=True)
        #print(W2)
        V2 = sorted(V, reverse=True)
        #print(V2)
        ans = 0
        for i in range(len(X3)):
            for j in range(len(W2)):
                if X3[i] >= W2[j]:
                    ans += V2[j]
                    break
        print(ans)
solve()

if __name__ == '__main__':
    solve()