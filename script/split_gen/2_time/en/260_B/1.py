def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = []
    for i in range(N):
        C.append([A[i], B[i], A[i]+B[i], i+1])
    C.sort(key=lambda x: x[2], reverse=True)
    C.sort(key=lambda x: x[1], reverse=True)
    C.sort(key=lambda x: x[0], reverse=True)
    for i in range(X):
        print(C[i][3])
    for i in range(X, X+Y):
        print(C[i][3])
    for i in range(X+Y, X+Y+Z):
        print(C[i][3])
