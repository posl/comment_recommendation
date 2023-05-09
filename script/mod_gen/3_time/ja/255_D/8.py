def main():
    N,Q=map(int,input().split())
    A=list(map(int,input().split()))
    X=[int(input()) for _ in range(Q)]
    S=sum(A)
    Ss=[0 for _ in range(N+1)]
    for i in range(N):
        Ss[i+1]=Ss[i]+A[i]
    for x in X:
        if x>S:
            print(N*(x-S)+sum([i*(Ss[i]-Ss[i-1]) for i in range(1,N+1)]))
        else:
            l,r=0,N
            while l+1<r:
                m=(l+r)//2
                if Ss[m]<=x*m:
                    l=m
                else:
                    r=m
            print(sum([i*(Ss[i]-Ss[i-1]) for i in range(1,l+1)])+(l+1)*(x*l-Ss[l]))

if __name__ == '__main__':
    main()