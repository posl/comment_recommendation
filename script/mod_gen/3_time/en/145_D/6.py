def main():
    X, Y = map(int, input().split())
    if (X + Y) % 3 != 0:
        print(0)
        return
    N = (X + Y) // 3
    if X > N or Y > N:
        print(0)
        return
    MOD = 10 ** 9 + 7
    fact = [1] * (N + 1)
    factinv = [1] * (N + 1)
    for i in range(1, N + 1):
        fact[i] = fact[i - 1] * i % MOD
        factinv[i] = pow(fact[i], MOD - 2, MOD)
    ans = fact[N] * factinv[X] * factinv[Y] % MOD
    print(ans)

if __name__ == '__main__':
    main()