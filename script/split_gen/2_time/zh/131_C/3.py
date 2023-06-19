def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
a,b,c,d=map(int,input().split())
g=gcd(c,d)
lcm=c*d//g
print(b-a+1-(b//c-(a-1)//c)-(b//d-(a-1)//d)+(b//lcm-(a-1)//lcm))
