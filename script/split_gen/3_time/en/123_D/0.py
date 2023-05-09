def main():
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    ABC = []
    for i in range(X):
        for j in range(Y):
            for k in range(Z):
                ABC.append(A[i] + B[j] + C[k])
    ABC.sort(reverse=True)
    for i in range(K):
        print(ABC[i])
