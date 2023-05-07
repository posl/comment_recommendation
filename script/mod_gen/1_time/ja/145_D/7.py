def main():
    x,y = map(int, input().split())
    if (x+y)%3 != 0:
        print(0)
        return
    else:
        n = (x+y)//3
    if x < n or y < n:
        print(0)
        return
    else:
        x -= n
        y -= n
    MOD = 10**9+7
    fac = [1, 1]
    finv = [1, 1]
    inv = [0, 1]
    for i in range(2, n+1):
        fac.append(fac[i-1] * i % MOD)
        inv.append(MOD - inv[MOD%i] * (MOD//i) % MOD)
        finv.append(finv[i-1] * inv[i] % MOD)
    def comb(n, r, MOD):
        if r < 0 or r > n:
            return 0
        else:
            return fac[n] * (finv[r] * finv[n-r] % MOD) % MOD
    print(comb(x+y, x, MOD))

if __name__ == '__main__':
    main()