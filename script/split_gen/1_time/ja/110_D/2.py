def main():
    N, M = map(int, input().split())
    mod = 10**9 + 7
    # 素因数分解
    def prime_factorize(n):
        a = []
        while n % 2 == 0:
            a.append(2)
            n //= 2
        f = 3
        while f * f <= n:
            if n % f == 0:
                a.append(f)
                n //= f
            else:
                f += 2
        if n != 1:
            a.append(n)
        return a
    # 素因数の種類数
    def prime_factorize_kind(n):
        return len(set(prime_factorize(n)))
    # 素因数の種類数の重複組み合わせ
    def prime_factorize_kind_comb(n, r):
        return factorial(n+r-1)//(factorial(r)*factorial(n-1))
    # 素因数の種類数の重複組み合わせの和
    def prime_factorize_kind_comb_sum(n, r):
        return sum(prime_factorize_kind_comb(n, i) for i in range(1, r+1))
    # 階乗
    def factorial(n):
        return 1 if n == 0 else n * factorial(n-1)
    # 組み合わせ
    def comb(n, r):
        return factorial(n) // (factorial(n - r) * factorial(r))
    # 重複組み合わせ
    def comb_rep(n, r):
        return comb(n+r-1, r)
    # 重複組み合わせの和
    def comb_rep_sum(n, r):
        return sum(comb_rep(n, i) for i in range(1, r+1))
    # 重複組み合わせの和
    def comb_rep_sum(n, r):
        return sum(comb_rep(n, i) for i in range(1, r+1))
    # 素因数の種類数の重複組み合わせの和
    def prime_factorize_kind_comb_sum(n, r
