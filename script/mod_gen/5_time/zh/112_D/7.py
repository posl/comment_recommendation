def gcd(a,b):
    if a<b:
        a,b=b,a
    while a%b!=0:
        a,b=b,a%b
    return b
N,M=map(int,input().split())
a=gcd(N,M)
print(M//a)

if __name__ == '__main__':
    gcd()