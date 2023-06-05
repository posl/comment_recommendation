def gcd(a,b):
    if a<b:
        a,b=b,a
    while b!=0:
        a,b=b,a%b
    return a
n,x=map(int,input().split())
a=list(map(int,input().split()))
a.append(x)
a.sort()
d=a[1]-a[0]
for i in range(2,n+1):
    d=gcd(d,a[i]-a[i-1])
print(d)
