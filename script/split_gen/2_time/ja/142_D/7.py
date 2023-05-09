def gcd(a,b):
    if a%b==0:
        return b
    return gcd(b,a%b)
a,b=map(int,input().split())
g=gcd(a,b)
print(len([i for i in range(1,g+1) if g%i==0]))
