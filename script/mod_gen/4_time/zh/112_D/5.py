def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
n, m = map(int, input().split())
#n, m = 3, 14
#n, m = 10, 123
#n, m = 100000, 1000000000

if __name__ == '__main__':
    gcd()