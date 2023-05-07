def main():
    N,X,Y,Z = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = [0]*N
    for i in range(N):
        C[i] = A[i]+B[i]
    D = [0]*N
    for i in range(N):
        D[i] = (C[i],A[i],i+1)
    D.sort(reverse=True)
    E = [0]*N
    for i in range(N):
        E[i] = (D[i][1],B[D[i][2]-1],D[i][2])
    E.sort(reverse=True)
    F = [0]*N
    for i in range(N):
        F[i] = (E[i][0]+E[i][1],E[i][2])
    F.sort(reverse=True)
    for i in range(X+Y+Z):
        print(F[i][1])

if __name__ == '__main__':
    main()