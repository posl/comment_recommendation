def solve():
    n,m=map(int,input().split())
    if m==0:
        print(1)
        return
    a=list(map(int,input().split()))
    a.sort()
    if a[0]!=1:
        a.append(0)
    a.append(n+1)
    a.sort()
    k=[]
    for i in range(1,len(a)):
        k.append(a[i]-a[i-1]-1)
    k.sort()
    if k[0]==0:
        k.pop(0)
    if k==[]:
        print(0)
        return
    ans=0
    for i in range(len(k)):
        ans+=k[i]//(k[0]+1)
        if k[i]%(k[0]+1)!=0:
            ans+=1
    print(ans)
solve()
