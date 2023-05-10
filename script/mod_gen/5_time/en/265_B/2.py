def main():
    N,M,T = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    Y = []
    for i in range(M):
        x,y = map(int, input().split())
        X.append(x)
        Y.append(y)
    
    for i in range(M):
        if i == 0:
            if T - A[X[i]-1] + Y[i] > 0:
                T = T - A[X[i]-1] + Y[i]
            else:
                print("No")
                return
        else:
            if T - A[X[i]-X[i-1]-1] + Y[i] - A[X[i-1]-1] > 0:
                T = T - A[X[i]-X[i-1]-1] + Y[i] - A[X[i-1]-1]
            else:
                print("No")
                return
    
    if T - A[N-1-X[M-1]-1] > 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()