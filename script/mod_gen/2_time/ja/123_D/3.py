def main():
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    S = []
    for i in range(X):
        for j in range(Y):
            S.append(A[i] + B[j])
    S.sort(reverse=True)
    T = []
    for i in range(min(K, X * Y)):
        for j in range(Z):
            T.append(S[i] + C[j])
    T.sort(reverse=True)
    for i in range(K):
        print(T[i])

if __name__ == '__main__':
    main()