def main():
    N,X,Y,Z = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = []
    for i in range(N):
        C.append([i+1,A[i],B[i]])
    C.sort(key=lambda x: x[0])
    C.sort(key=lambda x: x[2],reverse=True)
    C.sort(key=lambda x: x[1],reverse=True)
    for i in range(X):
        print(C[i][0])
    for i in range(X,X+Y):
        print(C[i][0])
    for i in range(X+Y,X+Y+Z):
        print(C[i][0])
