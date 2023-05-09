def main():
    # 入力
    N, M = map(int, input().split())
    # 素因数分解
    prime_factorization = {}
    i = 2
    while i*i <= M:
        if M%i == 0:
            prime_factorization[i] = 0
            while M%i == 0:
                M //= i
                prime_factorization[i] += 1
        i += 1
    if M > 1:
        prime_factorization[M] = 1
    # 出力
    ans = 1
    for k, v in prime_factorization.items():
        ans *= combination(v+N-1, N-1)
        ans %= MOD
    print(ans)
