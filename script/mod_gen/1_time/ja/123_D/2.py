def main():
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    L = []
    for i in range(X):
        for j in range(Y):
            L.append(A[i] + B[j])
    L.sort(reverse=True)
    M = []
    for i in range(min(K, X * Y)):
        for j in range(Z):
            M.append(L[i] + C[j])
    M.sort(reverse=True)
    for i in range(K):
        print(M[i])

if __name__ == '__main__':
    main()