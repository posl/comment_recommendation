def gcd(a,b):
    if a == 0 or b == 0:
        return 0
    while b != 0:
        a,b = b,a%b
    return a
