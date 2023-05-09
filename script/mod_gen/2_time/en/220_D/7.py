def main():
    N=int(input())
    A=list(map(int,input().split()))
    #print(A)
    MOD=998244353
    ans=[0]*10
    if N==2:
        ans[(A[0]+A[1])%10]=1
        ans[(A[0]*A[1])%10]=1
        print(*ans,sep='
')
        return
    for k in range(10):
        a=[0]*N
        b=[0]*N
        for i in range(N):
            a[i]=(A[i]+k)%10
            b[i]=(A[i]*k)%10
        #print(a)
        #print(b)
        for i in range(N-1):
            if a[i]==0:
                a[i+1]=(a[i+1]+10)%10
            if b[i]==0:
                b[i+1]=(b[i+1]+10)%10
        #print(a)
        #print(b)
        for i in range(N-1):
            if a[i]==0:
                a[i+1]=(a[i+1]+10)%10
            if b[i]==0:
                b[i+1]=(b[i+1]+10)%10
        #print(a)
        #print(b)
        for i in range(N-1):
            if a[i]==0:
                a[i+1]=(a[i+1]+10)%10
            if b[i]==0:
                b[i+1]=(b[i+1]+10)%10
        #print(a)
        #print(b)
        for i in range(N-1):
            if a[i]==0:
                a[i+1]=(a[i+1]+10)%10
            if b[i]==0:
                b[i+1]=(b[i+1]+10)%10
        #print(a)
        #print(b)
        for i in range(N-1):
            if a[i]==0:
                a[i+1]=(a[i+1]+10)%10
            if b[i]==0:
                b[i+1]=(b[i+1]+10)%10
        #print(a)
        #print(b)
        for i in range(N-1):
            if a[i]==0:
                a[i+1]=(a[i+1]+10)%10
            if b[i]==0:

if __name__ == '__main__':
    main()