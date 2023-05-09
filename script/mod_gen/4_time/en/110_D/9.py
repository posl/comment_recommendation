def main():
    N, M = map(int, input().split())
    MOD = 10**9+7
    # Mの素因数分解
    prime_factor = {}
    tmp = M
    i = 2
    while i**2 <= tmp:
        if tmp % i == 0:
            cnt = 0
            while tmp % i == 0:
                tmp //= i
                cnt += 1
            prime_factor[i] = cnt
        i += 1
    if tmp != 1:
        prime_factor[tmp] = 1
    #print(prime_factor)
    # 素因数の指数の組み合わせ
    # ex. M = 12 -> {2: 2, 3: 1} -> 3C0 + 3C1 + 3C2 = 8
    ans = 1
    for p, e in prime_factor.items():
        ans *= combination(e + N - 1, N - 1, MOD)
        ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()