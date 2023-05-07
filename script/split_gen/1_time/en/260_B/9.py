def main():
    N, X, Y, Z = map(int, input().split())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    #print(N, X, Y, Z)
    #print(A)
    #print(B)
    C = []
    for i in range(N):
        C.append([A[i], B[i], i+1])
    #print(C)
    C.sort(key=lambda x: x[2])
    C.sort(key=lambda x: x[1], reverse=True)
    C.sort(key=lambda x: x[0], reverse=True)
    #print(C)
    for i in range(X):
        print(C[i][2])
    for i in range(Y):
        print(C[i+X][2])
    for i in range(Z):
        print(C[i+X+Y][2])
