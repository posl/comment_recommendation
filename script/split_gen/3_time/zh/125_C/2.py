def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
n=int(input())
a=list(map(int,input().split()))
l=[0]*n
r=[0]*n
l[0]=a[0]
r[n-1]=a[n-1]
for i in range(1,n):
    l[i]=gcd(l[i-1],a[i])
    r[n-1-i]=gcd(r[n-i],a[n-1-i])
ans=max(l[n-2],r[1])
for i in range(1,n-1):
    ans=max(ans,gcd(l[i-1],r[i+1]))
print(ans)
