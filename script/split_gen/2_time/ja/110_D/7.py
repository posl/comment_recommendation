def main():
    N, M = map(int, input().split())
    mod = 10**9 + 7
    # 素因数分解
    def prime_factorization(n):
        # n の素因数分解した結果を返す
        # 返り値は、{素因数: 素因数の数} の辞書
        # 例) 12 = 2^2 * 3^1 の場合、{2: 2, 3: 1} が返る
        result = {}
        i = 2
        while i * i <= n:
            while n % i == 0:
                if i in result:
                    result[i] += 1
                else:
                    result[i] = 1
                n //= i
            i += 1
        if n > 1:
            result[n] = 1
        return result
    # 素因数分解
    prime = prime_factorization(M)
    # 約数の数
    def divisor_count(n):
        # n の約数の数を返す
        # 例) 12 の約数は 1, 2, 3, 4, 6, 12 なので、6 が返る
        result = 1
        for i in prime.values():
            result *= (i + 1)
        return result
    # 組み合わせ
    # nCk = n! / (k! * (n-k)!)
    def combination(n, k):
        # nCk を返す
        # ただし、返り値は 10^9 + 7 で割った余り
        # 例) 5C2 = 10
        result = 1
        for i in range(k):
            result *= (n - i)
            result %= mod
        for i in range(1, k + 1):
            result *= pow(i, mod - 2, mod)
            result %= mod
        return result
    print(combination(divisor_count(M), N))
