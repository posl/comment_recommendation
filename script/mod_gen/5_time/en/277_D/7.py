def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    # print(N, M, A)
    if M == 1:
        print(0)
        return
    if N == 1:
        print(A[0])
        return
    if N == 2:
        if A[1] == A[0] or A[1] == (A[0]+1)%M:
            print(A[0])
        else:
            print(A[0]+A[1])
        return
    X = []
    for i in range(N):
        X.append(A[i])
    # print(X)
    for i in range(1, N):
        if X[i] == X[i-1] or X[i] == (X[i-1]+1)%M:
            X[i] = 0
        else:
            break
    # print(X)
    for i in range(N-2, -1, -1):
        if X[i] == X[i+1] or X[i] == (X[i+1]+1)%M:
            X[i] = 0
        else:
            break
    # print(X)
    if X[0] == 0:
        print(0)
        return
    if X[-1] == 0:
        print(X[0])
        return
    if X[0] == X[-1]:
        print(X[0])
        return
    if X[0] == (X[-1]+1)%M:
        print(X[0])
        return
    print(X[0]+X[-1])

if __name__ == '__main__':
    main()