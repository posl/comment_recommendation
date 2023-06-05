def main():
    n=int(input())
    a=list(map(int,input().split()))
    p,q,r,s=0,0,0,0
    ans=10**9
    for i in range(n-3):
        p+=a[i]
        q=0
        for j in range(i+1,n-2):
            q+=a[j]
            r=0
            for k in range(j+1,n-1):
                r+=a[k]
                s=sum(a)-p-q-r
                ans=min(ans,max(p,q,r,s)-min(p,q,r,s))
    print(ans)
main()
