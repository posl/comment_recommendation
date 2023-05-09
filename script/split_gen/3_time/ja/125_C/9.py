def gcd(a,b):
    if a<b:
        a,b=b,a
    while b!=0:
        a,b=b,a%b
    return a
N=int(input())
A=list(map(int,input().split()))
gcd_max=0
for i in range(N):
    gcd_max=gcd(gcd_max,A[i])
print(gcd_max)
