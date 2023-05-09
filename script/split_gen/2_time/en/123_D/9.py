def solve(X, Y, Z, K, A, B, C):
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    AB = []
    for i in range(X):
        for j in range(Y):
            AB.append(A[i] + B[j])
    AB.sort(reverse=True)
    ABC = []
    for i in range(min(K, X * Y)):
        for j in range(Z):
            ABC.append(AB[i] + C[j])
    ABC.sort(reverse=True)
    for i in range(K):
        print(ABC[i])
