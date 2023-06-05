def main():
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=[0]*(n+1)
    for i in range(n):
        b[i+1]=b[i]+a[i]
    c=[0]*m
    for i in range(n+1):
        c[b[i]%m]+=1
    ans=c[0]
    for i in range(m):
        ans+=c[i]*(c[i]-1)//2
    print(ans)

if __name__ == '__main__':
    main()