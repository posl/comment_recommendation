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
pf = prime_factorize(N)
pf_set = set(pf)
ans = 0
for x in pf_set:
    i = 0
    while True:
        if x**(i+1) > N:
            ans = max(ans, i)
            break
        else:
            i += 1
print(ans)

if __name__ == '__main__':
    prime_factorize()