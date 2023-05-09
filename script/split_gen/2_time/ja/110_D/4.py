def main():
    N, M = map(int, input().split())
    # 素因数分解
    prime_factor = {}
    for i in range(2, int(M**(1/2)) + 1):
        while M % i == 0:
            prime_factor[i] = prime_factor.get(i, 0) + 1
            M //= i
    if M != 1:
        prime_factor[M] = 1
    # 素因数分解した結果を使って計算
    # 素因数分解した結果の個数を足し合わせる
    # その個数が N 以上になるような組み合わせの数を求める
    # その組み合わせの数を足し合わせる
    # その組み合わせの数は 10^9 + 7 で割った余りを求める
    ans = 1
    for p, n in prime_factor.items():
        ans *= combination(n + N - 1, n)
        ans %= 10**9 + 7
    print(ans)
