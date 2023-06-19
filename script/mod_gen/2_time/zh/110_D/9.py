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
n,m = map(int,input().split())
mod = 10**9+7
pf = prime_factorize(m)
pf.sort()
pf.append(0)
ans = 1
cnt = 0
for i in range(len(pf)-1):
    cnt += 1
    if pf[i] != pf[i+1]:
        ans *= cnt
        ans %= mod
        cnt = 0
ans *= pow(2,n-1,mod)
ans %= mod
print(ans)

if __name__ == '__main__':
    prime_factorize()