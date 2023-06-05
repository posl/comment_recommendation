def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
n,a,b = map(int,input().split())
g = gcd(a,b)
