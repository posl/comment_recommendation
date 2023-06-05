def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
n, m = map(int, input().split())
a = gcd(n, m)
print(m // a)

if __name__ == '__main__':
    gcd()