def gcd(a, b):
    if b > a:
        a, b = b, a
    while b > 0:
        a, b = b, a % b
    return a
a, b = map(int, input().split())
c = gcd(a, b)
print(a * b // c)

if __name__ == '__main__':
    gcd()