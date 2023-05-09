def main():
    N,X,Y,Z = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = [A[i]+B[i] for i in range(N)]
    A = [(A[i],i+1) for i in range(N)]
    B = [(B[i],i+1) for i in range(N)]
    C = [(C[i],i+1) for i in range(N)]
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    D = []
    for i in range(X):
        D.append(A[i][1])
    for i in range(Y):
        D.append(B[i][1])
    for i in range(Z):
        D.append(C[i][1])
    D.sort()
    for i in range(X+Y+Z):
        print(D[i])
