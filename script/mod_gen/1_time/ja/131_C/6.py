def gcd(a,b):
    if b > a:
        a,b = b,a
    while b != 0:
        a,b = b,a%b
    return a

if __name__ == '__main__':
    gcd()