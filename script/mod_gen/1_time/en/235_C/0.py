def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    K = []
    for i in range(Q):
        x, k = map(int, input().split())
        X.append(x)
        K.append(k)
    #print(N, Q)
    #print(A)
    #print(X)
    #print(K)
    for i in range(Q):
        count = 0
        for j in range(N):
            if A[j] == X[i]:
                count += 1
            if count == K[i]:
                print(j+1)
                break
        else:
            print(-1)
main()

if __name__ == '__main__':
    main()