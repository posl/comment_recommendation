def gcd(x,y):
    if x < y:
        x,y = y,x
    while y > 0:
        x,y = y,x % y
    return x

if __name__ == '__main__':
    gcd()