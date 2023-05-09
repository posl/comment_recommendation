def prime_factorization(n):
    ret = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                cnt += 1
                n //= i
            ret.append([i, cnt])
    if n != 1:
        ret.append([n, 1])
    return ret
n = int(input())
ans = 0
for p, e in prime_factorization(n):
    for i in range(1, e + 1):
        ans += 1
        e -= i
print(ans)
