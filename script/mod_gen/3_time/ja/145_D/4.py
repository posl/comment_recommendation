def main():
    x, y = map(int, input().split())
    if (x+y)%3 != 0:
        print(0)
        return
    n = (x+y)//3
    if x < n or y < n:
        print(0)
        return
    mod = 10**9+7
    def comb(n, r):
        if r < 0 or r > n:
            return 0
        r = min(r, n-r)
        return fac[n] * finv[r] % mod * finv[n-r] % mod
    N = 2*n
    fac = [1, 1]
    finv = [1, 1]
    inv = [0, 1]
    for i in range(2, N+1):
        fac.append(fac[-1] * i % mod)
        inv.append(mod - inv[mod%i] * (mod//i) % mod)
        finv.append(finv[-1] * inv[-1] % mod)
    print(comb(N, n))

if __name__ == '__main__':
    main()