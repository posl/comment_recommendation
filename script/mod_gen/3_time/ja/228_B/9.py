def main():
    N,X=map(int,input().split())
    A=list(map(int,input().split()))
    A=[a-1 for a in A]
    #print(N,X,A)
    ans=0
    f=[0 for _ in range(N)]
    while f[X-1]==0:
        f[X-1]=1
        X=A[X-1]
        ans+=1
    print(ans)

if __name__ == '__main__':
    main()