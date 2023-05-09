def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
n,m=map(int,input().split())
a=list(map(int,input().split()))
l=[0]*(m+1)
for i in range(n):
    for j in range(1,m+1):
        if gcd(a[i],j)==1:
            l[j]+=1
print(l.count(n))
for i in range(1,m+1):
    if l[i]==n:
        print(i)
