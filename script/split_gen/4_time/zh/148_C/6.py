def gcd(a,b): #最大公约数
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)
