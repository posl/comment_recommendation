def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
a,b,k=map(int,input().split())
g=gcd(a,b)
lcm=a*b//g
ans=0
for i in range(lcm,0,-1):
    if a%i==0 and b%i==0:
        k-=1
        if k==0:
            ans=i
            break
print(ans)
