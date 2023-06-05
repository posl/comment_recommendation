def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
b=[0]*(m+1)
for i in a:
    for j in range(i,m+1,i):
        b[j]+=1
ans=0
for i in range(1,m+1):
    if b[i]==1:
        ans+=1
print(ans)
for i in range(1,m+1):
    if b[i]==1:
        print(i)
