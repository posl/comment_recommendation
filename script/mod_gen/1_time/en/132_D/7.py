def main():
    N, K = map(int, input().split())
    MOD = 10**9 + 7
    fac = [1]
    for i in range(1, N+1):
        fac.append(fac[-1]*i%MOD)
    finv = [pow(fac[-1], MOD-2, MOD)]
    for i in range(N, 0, -1):
        finv.append(finv[-1]*i%MOD)
    finv.reverse()
    def comb(n, r):
        if n < r or n < 0 or r < 0:
            return 0
        return fac[n]*finv[r]*finv[n-r]%MOD
    for i in range(1, K+1):
        print(comb(N-K+1, i)*comb(K-1, i-1)%MOD)

if __name__ == '__main__':
    main()