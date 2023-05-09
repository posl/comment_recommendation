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
        #print("L, R", L, R)
        X2 = X[:L-1] + X[R:]
        X2.sort()
        #print("X2", X2)
        W2 = W[:]
        V2 = V[:]
        for j in range(M - R + L - 1):
            for k in range(N):
                if W2[k] <= X2[j]:
                    W2[k] = 0
                    V2[k] = 0
        #print("W2", W2)
        #print("V2", V2)
        ans = 0
        for j in range(N):
            ans += V2[j]
        print(ans)
