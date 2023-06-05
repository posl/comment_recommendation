def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
a, b = map(int, input().split())
x = gcd(a, b)
print(a * b // x)

if __name__ == '__main__':
    gcd()