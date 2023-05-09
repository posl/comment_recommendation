def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [A[i] + B[i] for i in range(N)]
    A = [(i, A[i]) for i in range(N)]
    B = [(i, B[i]) for i in range(N)]
    C = [(i, C[i]) for i in range(N)]
    A.sort(key=lambda x: x[1], reverse=True)
    B.sort(key=lambda x: x[1], reverse=True)
    C.sort(key=lambda x: x[1], reverse=True)
    A = [x[0] for x in A]
    B = [x[0] for x in B]
    C = [x[0] for x in C]
    for i in range(X):
        print(A[i] + 1)
    for i in range(Y):
        if B[i] not in A[:X]:
            print(B[i] + 1)
    for i in range(Z):
        if C[i] not in A[:X] and C[i] not in B[:Y]:
            print(C[i] + 1)
