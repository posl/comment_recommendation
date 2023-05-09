def get_gcd(a, b):
    if b == 0:
        return a
    else:
        return get_gcd(b, a % b)

if __name__ == '__main__':
    get_gcd()