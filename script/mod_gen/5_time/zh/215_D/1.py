def gcd(x,y):
    if x < y:
        x,y = y,x
    while y != 0:
        r = x % y
        x = y
        y = r
    return x

if __name__ == '__main__':
    gcd()