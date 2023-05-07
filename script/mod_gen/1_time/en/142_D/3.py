def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
a, b = map(int, input().split())
c = gcd(a, b)
ans = 1
for i in range(2, int(c**0.5)+1):
    if c % i == 0:
        ans += 1
        while c % i == 0:
            c //= i

if __name__ == '__main__':
    gcd()