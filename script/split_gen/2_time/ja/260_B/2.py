def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = []
    for i in range(N):
        C.append([A[i], B[i], i+1])
    C.sort(reverse=True)
    for i in range(X):
        print(C[i][2])
    C = C[X:]
    C.sort(key=lambda x: x[1], reverse=True)
    for i in range(Y):
        print(C[i][2])
    C = C[Y:]
    C.sort(key=lambda x: x[0]+x[1], reverse=True)
    for i in range(Z):
        print(C[i][2])
