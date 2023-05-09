def main():
    N, M = map(int, input().split())
    # 素因数分解
    prime_factor = {}
    n = M
    i = 2
    while i * i <= n:
        if n % i != 0:
            i += 1
            continue
        ex = 0
        while n % i == 0:
            ex += 1
            n //= i
        prime_factor[i] = ex
    if n != 1:
        prime_factor[n] = 1
    # 約数の個数を求める
    ans = 1
    for p, e in prime_factor.items():
        ans *= e + 1
        ans %= 10 ** 9 + 7
    # 約数の個数から組み合わせを求める
    print(pow(ans, N, 10 ** 9 + 7))
