def main():
    N, M = map(int, input().split())
    mod = 10**9 + 7
    # Mの素因数分解
    prime_factor = {}
    for i in range(2, int(M**0.5)+1):
        while M % i == 0:
            prime_factor[i] = prime_factor.get(i, 0) + 1
            M //= i
    if M != 1:
        prime_factor[M] = prime_factor.get(M, 0) + 1
    
    # 素因数ごとに、N個のボールを分ける場合の数を求める
    ans = 1
    for v in prime_factor.values():
        ans *= (v + N - 1) * pow(v, mod-2, mod) % mod
        ans %= mod
    print(ans)
