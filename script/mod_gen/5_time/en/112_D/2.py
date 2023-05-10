def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
n, m = map(int, input().split())
d = gcd(n, m)
print(m // d)

if __name__ == '__main__':
    gcd()