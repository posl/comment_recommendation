def main():
    N,X,Y,Z = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = []
    for i in range(N):
        C.append((A[i],B[i],i+1))
    C.sort(key=lambda x: x[0], reverse=True)
    C = C[:X]
    C.sort(key=lambda x: x[1], reverse=True)
    C = C[:X+Y]
    C.sort(key=lambda x: x[0]+x[1], reverse=True)
    C = C[:X+Y+Z]
    C.sort(key=lambda x: x[2])
    for i in range(X+Y+Z):
        print(C[i][2])

if __name__ == '__main__':
    main()