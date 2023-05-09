def main():
    X, Y = map(int, input().split())
    if (X + Y) % 3 != 0:
        print(0)
        return
    n = (X + Y) // 3
    if X - n < 0 or Y - n < 0:
        print(0)
        return
    X -= n
    Y -= n
    mod = 10**9 + 7
    fac = [1]
    for i in range(1, n + 1):
        fac.append(fac[-1] * i % mod)
    finv = [pow(fac[-1], mod - 2, mod)]
    for i in range(n, 0, -1):
        finv.append(finv[-1] * i % mod)
    finv.reverse()
    def comb(n, r):
        if n < r:
            return 0
        return fac[n] * finv[r] * finv[n - r] % mod
    print(comb(X + Y, X))

if __name__ == '__main__':
    main()