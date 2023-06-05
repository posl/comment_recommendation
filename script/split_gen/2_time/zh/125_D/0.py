def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)
n=int(input())
a=list(map(int,input().split()))
b=[0]*n
b[0]=a[0]
for i in range(1,n):
    b[i]=gcd(b[i-1],a[i])
print(b[n-1])
