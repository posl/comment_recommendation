def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)
n,m=map(int,input().split())

if __name__ == '__main__':
    gcd()