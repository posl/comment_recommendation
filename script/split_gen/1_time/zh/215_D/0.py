def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
n,m=map(int,input().split())
a=list(map(int,input().split()))
ans=[]
ans.append(1)
for i in range(2,m+1):
    flag=0
    for j in range(n):
        if gcd(a[j],i)!=1:
            flag=1
            break
    if flag==0:
        ans.append(i)
print(len(ans))
for i in ans:
    print(i)
