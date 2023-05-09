def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
n = int(input())
print(int(n / gcd(n, 2) * 2))

if __name__ == '__main__':
    gcd()