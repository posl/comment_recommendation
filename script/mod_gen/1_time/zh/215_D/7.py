def gcd(x,y):
    if x % y == 0:
        return y
    else:
        return gcd(y,x%y)

if __name__ == '__main__':
    gcd()