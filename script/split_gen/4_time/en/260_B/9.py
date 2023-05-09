def problem260_b():
    N,X,Y,Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(lambda x,y: x+y, A, B))
    D = list(zip(C, range(1,N+1)))
    D.sort(key=lambda x: x[1])
    D.sort(key=lambda x: x[0], reverse=True)
    for i in range(X):
        print(D[i][1])
    for i in range(X,X+Y):
        print(D[i][1])
    for i in range(X+Y,X+Y+Z):
        print(D[i][1])
