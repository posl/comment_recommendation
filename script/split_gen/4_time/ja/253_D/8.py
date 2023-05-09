def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
N,A,B = map(int,input().split())
lcm = A*B//gcd(A,B)
print((N//A+N//B-N//lcm)*A+(N//B-N//lcm)*B)
