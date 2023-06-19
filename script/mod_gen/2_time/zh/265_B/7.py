def main():
    N,M,T = map(int,input().split())
    A = list(map(int,input().split()))
    XY = [list(map(int,input().split())) for _ in range(M)]
    
    X = [0]*(N+1)
    Y = [0]*(N+1)
    for x,y in XY:
        X[x] = x
        Y[x] = y
    
    t = T
    for i in range(1,N):
        t -= A[i-1]
        if t <= 0:
            print("No")
            return
        t = min(T,t+Y[i])
    print("Yes")

if __name__ == '__main__':
    main()