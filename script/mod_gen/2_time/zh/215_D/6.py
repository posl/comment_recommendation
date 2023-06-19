def gcd(x,y):
    while x:
        x,y = y%x,x
    return y

if __name__ == '__main__':
    gcd()