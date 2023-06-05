def solve():
    N,M,T = map(int,input().split())
    A = list(map(int,input().split()))
    X = []
    Y = []
    for i in range(M):
        x,y = map(int,input().split())
        X.append(x)
        Y.append(y)
    #print(N,M,T,A,X,Y)
    #print("N = ",N)
    #print("M = ",M)
    #print("T = ",T)
    #print("A = ",A)
    #print("X = ",X)
    #print("Y = ",Y)
    #print("N = ",N)
    #print("M = ",M)
    #print("T = ",T)
    #print("A = ",A)
    #print("X = ",X)
    #print("Y = ",Y)
    for i in range(M):
        if X[i] == 1:
            T += Y[i]
    #print("T = ",T)
    for i in range(N-1):
        #print("A[",i,"] = ",A[i])
        T -= A[i]
        #print("T = ",T)
        if T <= 0:
            print("No")
            return
        for j in range(M):
            if X[j] == i+2:
                T += Y[j]
        #print("T = ",T)
    if T > 0:
        print("Yes")
    else:
        print("No")
    return
