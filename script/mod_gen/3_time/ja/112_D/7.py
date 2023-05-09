def gcd(a,b):
    if a<b:
        a,b=b,a
    while b!=0:
        a,b=b,a%b
    return a
n,m=map(int,input().split())
a=gcd(n,m)
print(m//a)

if __name__ == '__main__':
    gcd()