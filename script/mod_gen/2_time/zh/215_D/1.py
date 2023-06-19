def gcd(x,y):
    if x < y:
        x,y = y,x
    if y == 0:
        return x
    else:
        return gcd(y,x%y)

if __name__ == '__main__':
    gcd()