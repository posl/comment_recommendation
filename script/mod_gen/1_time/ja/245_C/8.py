def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    X = [0]*N
    #初期化
    X[0] = A[0]
    #print(X)
    for i in range(1,N):
        #print("i=",i)
        if abs(X[i-1]-A[i])<=K and abs(X[i-1]-A[i])<=abs(X[i-1]-B[i]):
            X[i] = A[i]
            #print("A",X)
        elif abs(X[i-1]-B[i])<=K and abs(X[i-1]-B[i])<=abs(X[i-1]-A[i]):
            X[i] = B[i]
            #print("B",X)
        else:
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    main()