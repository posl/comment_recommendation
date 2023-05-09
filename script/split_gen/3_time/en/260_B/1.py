def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = []
    for i in range(N):
        C.append([A[i], B[i], A[i] + B[i], i + 1])
    C.sort(key=lambda x: x[0], reverse=True)
    D = []
    for i in range(X):
        D.append(C[i])
    C.sort(key=lambda x: x[1], reverse=True)
    for i in range(Y):
        D.append(C[i])
    C.sort(key=lambda x: x[2], reverse=True)
    for i in range(Z):
        D.append(C[i])
    D.sort(key=lambda x: x[3])
    for i in range(len(D)):
        print(D[i][3])
