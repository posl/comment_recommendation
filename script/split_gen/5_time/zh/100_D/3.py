def main():
    n,m=map(int,input().split())
    x=[]
    y=[]
    z=[]
    for i in range(n):
        a,b,c=map(int,input().split())
        x.append(a)
        y.append(b)
        z.append(c)
    ans=0
    for i in range(2**3):
        k=[]
        for j in range(n):
            k.append(x[j]*(-1)**((i>>0)&1)+y[j]*(-1)**((i>>1)&1)+z[j]*(-1)**((i>>2)&1))
        k.sort(reverse=True)
        ans=max(ans,sum(k[:m]))
    print(ans)
