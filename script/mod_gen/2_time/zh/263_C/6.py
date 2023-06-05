def func():
    n=int(input())
    p=list(map(int,input().split()))
    p.insert(0,0)
    ans=0
    for i in range(1,n+1):
        cnt=0
        j=i
        while j!=1:
            j=p[j]
            cnt+=1
        ans=max(ans,cnt)
    print(ans+1)
func()
