def gcd(x,y):
    if x<y:
        x,y=y,x
    if y==0:
        return x
    return gcd(y,x%y)
n=int(input())
a=list(map(int,input().split()))
l=[0]*n
r=[0]*n
l[0]=a[0]
r[-1]=a[-1]
for i in range(1,n):
    l[i]=gcd(l[i-1],a[i])
for i in range(n-2,-1,-1):
    r[i]=gcd(r[i+1],a[i])
ans=0
for i in range(n):
    if i==0:
        ans=max(ans,r[i+1])
    elif i==n-1:
        ans=max(ans,l[i-1])
    else:
        ans=max(ans,gcd(l[i-1],r[i+1]))
print(ans)
