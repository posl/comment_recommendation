def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
a, b = map(int, input().split())
g = gcd(a, b)
print(a * b // g)

if __name__ == '__main__':
    gcd()