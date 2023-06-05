def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
a,b=map(int,input().split())
gcd_num=gcd(a,b)
print(a*b//gcd_num)
