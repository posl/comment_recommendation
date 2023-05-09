def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
A,B = map(int,input().split())
GCD = gcd(A,B)
LCM = int(A*B/GCD)
print(LCM)
