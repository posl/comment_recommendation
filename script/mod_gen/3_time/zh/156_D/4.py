def find_gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return find_gcd(b, a%b)

if __name__ == '__main__':
    find_gcd()