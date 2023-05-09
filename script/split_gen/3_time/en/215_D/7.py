def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
g=a[0]
for i in range(1,n):
    g=gcd(g,a[i])
c=0
for i in range(1,m+1):
    if(gcd(g,i)==1):
        c+=1
        print(i)
print(c)
