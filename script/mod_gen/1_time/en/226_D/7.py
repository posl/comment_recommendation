def find_gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

if __name__ == '__main__':
    find_gcd()