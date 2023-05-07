def main():
    N,M=map(int,input().split())
    A=list(map(int,input().split()))
    A.sort()
    A.append(N+1)
    if A[0]!=1:
        A.insert(0,0)
    if A[-1]!=N+1:
        A.append(N+1)
    #print(A)
    B=[]
    for i in range(1,len(A)):
        if A[i]-A[i-1]-1!=0:
            B.append(A[i]-A[i-1]-1)
    B.sort()
    if len(B)==0:
        print(0)
    else:
        k=B[0]
        ans=0
        for i in range(len(B)):
            ans+=B[i]//k
            if B[i]%k!=0:
                ans+=1
        print(ans)

if __name__ == '__main__':
    main()