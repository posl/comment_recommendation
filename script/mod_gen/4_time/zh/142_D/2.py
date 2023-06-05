def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
a, b = map(int, input().split())
g = gcd(a, b)
ans = 1
for i in range(2, int(g**0.5)+1):
    if g % i == 0:
        ans += 1
        while g % i == 0:
            g //= i

if __name__ == '__main__':
    gcd()