def main():
    a, b, k = map(int, input().split())
    def comb(n, r):
        if n < r:
            return 0
        else:
            r = min(r, n-r)
            return fact[n] * factinv[r] * factinv[n-r] % mod
    mod = 10**9 + 7
    n = a + b
    fact = [1, 1]
    factinv = [1, 1]
    inv = [0, 1]
    for i in range(2, n+1):
        fact.append((fact[-1] * i) % mod)
        inv.append((-inv[mod%i] * (mod//i)) % mod)
        factinv.append((factinv[-1] * inv[-1]) % mod)
    ans = []
    while a + b > 0:
        if a == 0:
            ans.append('b')
            b -= 1
            continue
        elif b == 0:
            ans.append('a')
            a -= 1
            continue
        num = comb(a+b-1, a-1)
        if k <= num:
            ans.append('a')
            a -= 1
        else:
            ans.append('b')
            b -= 1
            k -= num
    print(''.join(ans))

if __name__ == '__main__':
    main()