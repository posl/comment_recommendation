def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = sorted([(i, A[i], B[i], A[i] + B[i]) for i in range(N)], key=lambda x: (x[1], -x[0]), reverse=True)
    D = sorted([(i, A[i], B[i], A[i] + B[i]) for i in range(N)], key=lambda x: (x[2], -x[0]), reverse=True)
    E = sorted([(i, A[i], B[i], A[i] + B[i]) for i in range(N)], key=lambda x: (x[3], -x[0]), reverse=True)
    F = set()
    for i in range(X):
        F.add(C[i][0])
    for i in range(Y):
        F.add(D[i][0])
    for i in range(Z):
        F.add(E[i][0])
    for i in range(1, N + 1):
        if i in F:
            print(i)
