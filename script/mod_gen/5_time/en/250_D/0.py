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
N = int(input())
count = 0
for i in range(1, N+1):
    if i % 2 == 0:
        continue
    if i % 5 == 0:
        continue
    if prime_factorize(i).count(3) == 3:
        count += 1
print(count)

if __name__ == '__main__':
    prime_factorize()