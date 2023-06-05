def gcd(a,b):#最大公约数
    if a>b:
        a,b=b,a
    while a!=0:
        a,b=b%a,a
    return b

if __name__ == '__main__':
    gcd()