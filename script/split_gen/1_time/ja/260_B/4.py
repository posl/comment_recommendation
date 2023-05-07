def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [A[i] + B[i] for i in range(N)]
    #print(A)
    #print(B)
    #print(C)
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    #print(A)
    #print(B)
    #print(C)
    for i in range(X):
        print(A.index(A[i])+1)
    for i in range(Y):
        print(B.index(B[i])+1)
    for i in range(Z):
        print(C.index(C[i])+1)
