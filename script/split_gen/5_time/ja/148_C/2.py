def gcd(a,b):
    if b==0:return a
    return gcd(b,a%b)
a,b=map(int,input().split())
g=gcd(a,b)
l=a*b//g
print(l)
