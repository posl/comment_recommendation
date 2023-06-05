def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)
A,B=map(int,input().split())
g=gcd(A,B)
lcm=A*B//g
print(lcm)

if __name__ == '__main__':
    gcd()