def gcd(a,b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a >= b:
        return gcd(a%b,b)
    if a < b:
        return gcd(a,b%a)

if __name__ == '__main__':
    gcd()