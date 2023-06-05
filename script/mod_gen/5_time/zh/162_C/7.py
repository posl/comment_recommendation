def gcd(a,b,c):
    if a>b:
        a,b=b,a
    if b>c:
        b,c=c,b
    if a>b:
        a,b=b,a
    if a==0:
        return b
    else:
        return gcd(a,b%a,c)

if __name__ == '__main__':
    gcd()