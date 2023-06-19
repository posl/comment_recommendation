def gcd(x,y):
    while x:
        x,y = y%x,x
    return y
