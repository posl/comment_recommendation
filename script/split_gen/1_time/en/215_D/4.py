def gcd(a,b):
    if a<b:
        a,b=b,a
    if b==0:
        return a
    else:
        return gcd(b,a%b)
N,M=map(int,input().split())
A=list(map(int,input().split()))
