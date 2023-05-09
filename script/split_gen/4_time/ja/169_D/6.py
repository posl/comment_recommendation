def prime_factorize(N):
    a = []
    while N % 2 == 0:
        a.append(2)
        N //= 2
    f = 3
    while f * f <= N:
        if N % f == 0:
            a.append(f)
            N //= f
        else:
            f += 2
    if N != 1:
        a.append(N)
    return a
N = int(input())
pf = prime_factorize(N)
pf_set = set(pf)
pf_len = len(pf_set)
pf_count = [pf.count(x) for x in pf_set]
pf_count.sort(reverse=True)
ans = 0
for i in range(len(pf_count)):
    c = pf_count[i]
    ans += int((-1+(1+8*c)**0.5)/2)
print(ans)
