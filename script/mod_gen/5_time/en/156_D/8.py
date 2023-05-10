def main():
    n, a, b = map(int, input().split())
    MOD = 10**9 + 7
    if n < 2 * 10**5:
        fact = [1]
        for i in range(1, 2 * 10**5 + 1):
            fact.append((fact[-1] * i) % MOD)
        fact_inv = [pow(fact[-1], MOD - 2, MOD)]
        for i in range(2 * 10**5, 0, -1):
            fact_inv.append((fact_inv[-1] * i) % MOD)
        fact_inv.reverse()
    else:
        fact = [1]
        for i in range(1, n + 1):
            fact.append((fact[-1] * i) % MOD)
        fact_inv = [pow(fact[-1], MOD - 2, MOD)]
        for i in range(n, 0, -1):
            fact_inv.append((fact_inv[-1] * i) % MOD)
        fact_inv.reverse()
    def comb(n, r):
        return fact[n] * fact_inv[r] * fact_inv[n - r] % MOD
    print((pow(2, n, MOD) - comb(n, a) - comb(n, b) - 1) % MOD)
main()

if __name__ == '__main__':
    main()