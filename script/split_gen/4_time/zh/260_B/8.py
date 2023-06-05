def main():
    N,X,Y,Z=map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    C=[]
    for i in range(N):
        C.append([i+1,A[i],B[i]])
    C.sort(key=lambda x:(-x[1],x[0]))
    D=C[:X]
    D.sort(key=lambda x:(-x[2],x[0]))
    E=C[X:X+Y]
    E.sort(key=lambda x:(-(x[1]+x[2]),x[0]))
    F=C[X+Y:]
    F.sort(key=lambda x:x[0])
    for i in range(len(D)):
        print(D[i][0])
    for i in range(len(E)):
        print(E[i][0])
    for i in range(len(F)):
        print(F[i][0])
main()
