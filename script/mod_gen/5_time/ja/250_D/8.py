def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
n = int(input())
ans = 0
for i in range(2, n+1):
    if i % 2 == 0:
        continue
    if i % 5 == 0:
        continue
    if i % 7 == 0:
        continue
    if i % 11 == 0:
        continue
    if i % 13 == 0:
        continue
    if i % 17 == 0:
        continue
    if i % 19 == 0:
        continue
    if i % 23 == 0:
        continue
    if i % 29 == 0:
        continue
    if i % 31 == 0:
        continue
    if i % 37 == 0:
        continue
    if i % 41 == 0:
        continue
    if i % 43 == 0:
        continue
    if i % 47 == 0:
        continue
    if i % 53 == 0:
        continue
    if i % 59 == 0:
        continue
    if i % 61 == 0:
        continue
    if i % 67 == 0:
        continue
    if i % 71 == 0:
        continue
    if i % 73 == 0:
        continue
    if i % 79 == 0:
        continue
    if i % 83 == 0:
        continue
    if i % 89 == 0:
        continue
    if i % 97 == 0:
        continue
    if i % 101 == 0:
        continue
    if i % 103 == 0:
        continue
    if i % 107 == 0:
        continue
    if i % 109 == 0:
        continue
    if i % 113 == 0:
        continue
    if i % 127 == 0:
        continue

if __name__ == '__main__':
    prime_factorize()