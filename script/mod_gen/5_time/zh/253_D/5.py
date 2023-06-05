def gcd(a, b):
    while(b != 0):
        t = a % b
        a = b
        b = t
    return a

if __name__ == '__main__':
    gcd()