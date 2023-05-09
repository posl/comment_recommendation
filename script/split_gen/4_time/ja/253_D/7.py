def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
n,a,b = map(int,input().split())
g = gcd(a,b)
lcm = a*b//g
n1 = n//a
n2 = n//b
n3 = n//lcm
print(n*(n+1)//2 - (n1+n2-n3)*(a+b)//2)
