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
        #print(L, R)
        X2 = X.copy()
        for j in range(L, R+1):
            X2[j] = -1
        #print(X2)
        X3 = []
        for j in range(M):
            if X2[j] != -1:
                X3.append(X2[j])
        #print(X3)
        ans = 0
        for j in range(N):
            for k in range(len(X3)):
                if W[j] <= X3[k]:
                    ans += V[j]
                    X3[k] = -1
                    break
        print(ans)
        #print()

if __name__ == '__main__':
    main()