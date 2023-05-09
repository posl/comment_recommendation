def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a%b
    return a
n = int(input())
print(n*2//gcd(n, 2))

if __name__ == '__main__':
    gcd()