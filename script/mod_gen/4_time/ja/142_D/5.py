def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
a, b = map(int, input().split())
n = gcd(a, b)
cnt = 1
for i in range(2, int(n**0.5)+1):
    if n % i == 0:
        cnt += 1
        while n % i == 0:
            n //= i

if __name__ == '__main__':
    gcd()