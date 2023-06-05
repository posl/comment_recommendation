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
a = [0] * (N + 1)
for i in range(2, N + 1):
    for j in prime_factorize(i):
        a[j] += 1
ans = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        for k in range(j + 1, len(a)):
            if a[i] >= 4 and a[j] >= 4 and a[k] >= 2:
                ans += 1
            if a[i] >= 14 and a[k] >= 4:
                ans += 1
            if a[j] >= 4 and a[k] >= 4 and a[i] >= 2:
                ans += 1
print(ans)

if __name__ == '__main__':
    prime_factorize()