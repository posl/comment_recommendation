def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
n,x=map(int,input().split())
a=list(map(int,input().split()))
a.append(x)
a.sort()
b=[]
for i in range(n):
    b.append(a[i+1]-a[i])
d=b[0]
for i in range(n):
    d=gcd(d,b[i])
print(d)
