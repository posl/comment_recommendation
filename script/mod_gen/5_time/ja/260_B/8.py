def main():
    N,X,Y,Z = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = []
    for i in range(N):
        C.append([i+1,A[i],B[i],A[i]+B[i]])
    C.sort(key=lambda x:(-x[1],-x[2],-x[3],x[0]))
    for i in range(X):
        print(C[i][0])
    for i in range(X,X+Y):
        print(C[i][0])
    for i in range(X+Y,X+Y+Z):
        print(C[i][0])
main()

if __name__ == '__main__':
    main()