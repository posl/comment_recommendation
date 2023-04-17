Synthesizing 10/10 solutions

=======

def factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

=======

def main():
    N, M = map(int, input().split())
    mod = 10**9 + 7
    ans = 1
    for i in range(2, int(M**0.5) + 1):
        if M % i != 0:
            continue
        cnt = 0
        while M % i == 0:
            M //= i
            cnt += 1
        ans *= comb(N + cnt - 1, N - 1, mod)
        ans %= mod
    if M != 1:
        ans *= N
        ans %= mod
    print(ans)

=======

def main():
    n, m = map(int, input().split())
    ans = 1
    for i in range(2, int(m**0.5)+1):
        if m % i == 0:
            count = 0
            while m % i == 0:
                m //= i
                count += 1
            ans *= comb(count+n-1, n-1)
            ans %= 10**9+7
    if m != 1:
        ans *= n
        ans %= 10**9+7
    print(ans)

=======

def main():
    n, m = map(int, input().split())
    mod = 10**9 + 7
    ans = 1
    for i in range(2, m+1):
        if m % i == 0:
            cnt = 1
            while m % i == 0:
                m //= i
                cnt += 1
            ans = ans * cnt % mod
    print((ans + n - 1) % mod)

=======

def main():
    n, m = map(int, input().split())
    MOD = 10**9 + 7
    ans = 1
    i = 2
    while i*i <= m:
        if m%i == 0:
            cnt = 0
            while m%i == 0:
                m //= i
                cnt += 1
            ans *= cmb(cnt+n-1, n-1)
            ans %= MOD
        i += 1
    if m != 1:
        ans *= n
        ans %= MOD
    print(ans)

=======

def main():
    N, M = map(int, input().split())
    MOD = 10 ** 9 + 7
    # 素因数分解
    def prime_factorization(n):
        arr = []
        temp = n
        for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
            if temp % i == 0:
                cnt = 0
                while temp % i == 0:
                    cnt += 1
                    temp //= i
                arr.append([i, cnt])

        if temp != 1:
            arr.append([temp, 1])

        if arr == []:
            arr.append([n, 1])

        return arr

    # フェルマーの小定理を用いて逆元を求める
    def modinv(a, mod):
        return pow(a, mod - 2, mod)

    # 組み合わせの計算
    def cmb(n, r, mod):
        if (r < 0) or (n < r):
            return 0
        r = min(r, n - r)
        return g1[n] * g2[r] * g2[n - r] % mod

    # 階乗の計算
    def factorial(n, mod):
        v = 1
        for i in range(2, n + 1):
            v = (v * i) % mod
        return v

    # 1〜Nまでの階乗を計算
    mod = MOD
    N = M
    g1 = [1, 1]  # 元テーブル
    g2 = [1, 1]  # 逆元テーブル
    inverse = [0, 1]  # 逆元テーブル計算用テーブル

    for i in range(2, N + 1):
        g1.append((g1[-1] * i) % mod)
        inverse.append((-inverse[mod % i] * (mod // i)) % mod)
        g2.append((g2[-1] * inverse[-1]) % mod)

    # 答えを求める
    ans = 1

=======

def main():
    N, M = map(int, input().split())
    MOD = 10**9 + 7
    # a_1 * a_2 * ... * a_N = M
    # a_1 * a_2 * ... * a_N = p_1^e_1 * p_2^e_2 * ... * p_k^e_k
    # 1 <= a_i <= M
    # 1 <= N <= 10**5
    # 1 <= M <= 10**9
    # 1 <= e_i <= 10**5
    # p_i <= M
    # p_i = p_j (i != j) => e_i = e_j
    # p_1 * p_2 * ... * p_k <= M
    # p_1 * p_2 * ... * p_k = M
    # e_1 + e_2 + ... + e_k = N
    # e_1 <= N
    # e_2 <= N - e_1
    # ...
    # e_k <= N - e_1 - ... - e_{k-1}
    # e_1 + e_2 + ... + e_k = N
    # e_1 + e_2 + ... + e_k <= N
    # e_1 <= N - e_2 - ... - e_k
    # ...
    # e_k <= N - e_1 - ... - e_{k-1}
    # e_1 <= N - e_2 - ... - e_k
    # e_2 <= N - e_1 - e_3 - ... - e_k
    # e_3 <= N - e_1 - e_2 - ... - e_k
    # ...
    # e_k <= N - e_1 - e_2 - ... - e_{k-1}
    # e_1 <= N - e_2 - ... - e_k
    # e_2 <= N - e_1 - e_3 - ... - e_k
    # ...
    # e_k <= N - e_1 - e_2 - ... - e_{k-1}
    # e_1 <= N - e_2 - ... - e_k
    # e_2 <= N - e_1 - e_

=======

def main():
    N, M = map(int, input().split())
    MOD = 10**9 + 7
    # Mの素因数分解
    fact = []
    i = 2
    while i * i <= M:
        if M % i == 0:
            cnt = 0
            while M % i == 0:
                M //= i
                cnt += 1
            fact.append(cnt)
        i += 1
    if M > 1:
        fact.append(1)
    # print(fact)
    # 素因数分解した数の各個数からN個選ぶ組み合わせの数
    ans = 1
    for i in fact:
        ans *= comb(i + N - 1, N - 1, MOD)
        ans %= MOD
    print(ans)

=======

def main():
    N, M = map(int, input().split())
    MOD = 10 ** 9 + 7

    # Mの素因数分解
    # M = 2^a1 * 3^a2 * ... * p^an
    # この時、Mの約数の個数は(a1+1) * (a2+1) * ... * (an+1) である
    # 素因数分解した結果を素因数とその指数からなる辞書にする
    factors = {}
    i = 2
    while i * i <= M:
        if M % i != 0:
            i += 1
            continue
        ex = 0
        while M % i == 0:
            ex += 1
            M //= i
        factors[i] = ex
        i += 1
    if M != 1:
        factors[M] = 1

    # 約数の個数を求める
    ans = 1
    for k, v in factors.items():
        ans *= (v + 1)
        ans %= MOD

    # 約数の個数から答えを求める
    ans = pow(ans, N, MOD)
    print(ans)

=======

def get_prime_factors(n):
    """Return a list of prime factors of n."""
    if n < 2:
        return []
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n //= d
        d = d + 1
        if d*d > n:
            if n > 1:
                factors.append(n)
            break
    return factors
