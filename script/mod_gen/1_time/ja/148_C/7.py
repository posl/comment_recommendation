def gcd(x,y):
    if y == 0:
        return x
    return gcd(y,x%y)

if __name__ == '__main__':
    gcd()