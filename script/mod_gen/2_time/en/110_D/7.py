def main():
    N, M = map(int, input().split())
    MOD = 10**9 + 7
    # Mの素因数分解
    prime_factor = {}
    for i in range(2, int(M**0.5) + 1):
        while M % i == 0:
            M //= i
            prime_factor[i] = prime_factor.get(i, 0) + 1
    if M != 1:
        prime_factor[M] = 1
    # 素因数ごとに、N個選ぶ組み合わせの数を求める
    ans = 1
    for p in prime_factor.values():
        ans *= comb(N + p - 1, p)
        ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()