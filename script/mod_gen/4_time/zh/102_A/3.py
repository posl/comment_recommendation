def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
n=int(input())
print(int(2*n/gcd(2,n)))
