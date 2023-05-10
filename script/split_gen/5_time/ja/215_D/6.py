def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
n,m=map(int,input().split())
a=list(map(int,input().split()))
a=set(a)
l=[True]*(m+1)
for aa in a:
    for i in range(1,m+1):
        if i*aa>m:
            break
        l[i*aa]=False
ans=[]
for i in range(1,m+1):
    if l[i]:
        ans.append(i)
print(len(ans))
for a in ans:
    print(a)
