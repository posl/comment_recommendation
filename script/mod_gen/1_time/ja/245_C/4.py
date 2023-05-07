def main():
    N,K=map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    X=[0]*N
    for i in range(N):
        if i==0:
            X[0]=A[0]
            continue
        if A[i]==B[i]:
            X[i]=A[i]
            continue
        if abs(A[i]-B[i])<=K:
            X[i]=min(A[i],B[i])
            continue
        if A[i]<B[i]:
            X[i]=A[i]
            continue
        if A[i]>B[i]:
            X[i]=B[i]
            continue
    
    for i in range(N-1):
        if abs(X[i]-X[i+1])>K:
            print("No")
            return
    print("Yes")
    return
main()

if __name__ == '__main__':
    main()