def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
n, m = map(int, input().split())
for i in range(m // n, 0, -1):
    if m % i == 0 and gcd(i, m // i) == 1:
        print(i)
        break

if __name__ == '__main__':
    gcd()