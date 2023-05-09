def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
gcds=[0]*(m+1)
for i in range(n):
    for j in range(a[i],m+1,a[i]):
        gcds[j]=1
ans=[]
for i in range(1,m+1):
    if gcds[i]==0:
        ans.append(i)
print(len(ans))
for i in ans:
    print(i)
