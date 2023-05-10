def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
n,a,b=map(int,input().split())
lcm=a*b//gcd(a,b)
ans=n//a+n//b-n//lcm
print(ans)

if __name__ == '__main__':
    gcd()