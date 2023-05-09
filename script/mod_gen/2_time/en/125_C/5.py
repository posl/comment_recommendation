def gcd(a, b): # greatest common divisor
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

if __name__ == '__main__':
    gcd()