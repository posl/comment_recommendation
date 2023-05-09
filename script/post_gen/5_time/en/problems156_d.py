Synthesizing 10/10 solutions

=======
Suggestion 1

def combinations_count(n, r):
    if n < r:
        return 0
    r = min(n - r, r)
    if r == 0:
        return 1
    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]
    for p in range(2, r + 1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p - 1, r, p):
                numerator[k - offset] //= pivot
                denominator[k] //= pivot
    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= numerator[k]
    return result

n, a, b = map(int, input().split())
mod = 10**9 + 7

total = pow(2, n, mod) - 1
a_count = combinations_count(n, a)
b_count = combinations_count(n, b)

print((total - a_count - b_count) % mod)

=======
Suggestion 2

def main():
    n, a, b = map(int, input().split())
    mod = 10**9 + 7

    def comb(n, r):
        x, y = 1, 1
        for i in range(r):
            x = x * (n - i) % mod
            y = y * (i + 1) % mod
        return x * pow(y, mod - 2, mod) % mod

    print((pow(2, n, mod) - 1 - comb(n, a) - comb(n, b)) % mod)

=======
Suggestion 3

def main():
    n, a, b = map(int, input().split())

    if a > b:
        a, b = b, a

    if a + 1 == b:
        print(n * (n - 1) % 1000000007)
        return

    if a + 2 == b:
        print(n * (n - 1) % 1000000007 * (n - 2) % 1000000007)
        return

    print((n - a - 1) * (n - b - 1) % 1000000007)

main()

=======
Suggestion 4

def main():
    n, a, b = map(int, input().split())
    mod = 10 ** 9 + 7
    ans = pow(2, n, mod) - 1
    a_c = 1
    b_c = 1
    for i in range(a):
        a_c *= (n - i)
        a_c %= mod
        a_c *= pow(i + 1, mod - 2, mod)
        a_c %= mod
    for i in range(b):
        b_c *= (n - i)
        b_c %= mod
        b_c *= pow(i + 1, mod - 2, mod)
        b_c %= mod
    ans -= a_c
    ans %= mod
    ans -= b_c
    ans %= mod
    print(ans)

=======
Suggestion 5

def comb(n, r):
    if n - r < r:
        return comb(n, n - r)
    else:
        ans_mul = 1
        ans_div = 1
        for i in range(r):
            ans_mul *= n - i
            ans_div *= i + 1
        return ans_mul // ans_div

n, a, b = map(int, input().split())
ans = pow(2, n, 10**9 + 7) - 1
ans -= comb(n, a)
ans -= comb(n, b)
print(ans % (10**9 + 7))

=======
Suggestion 6

def countFlowers(n, a, b):
    count = 0
    for i in range(1, n+1):
        if i != a and i != b:
            count += 1
    return count

n, a, b = map(int, input().split())
print(countFlowers(n, a, b))

=======
Suggestion 7

def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)

=======
Suggestion 8

def comb(n, r):
    if n < r:
        return 0
    elif r == 0:
        return 1
    else:
        return comb(n-1, r-1) * n // r

n,a,b = map(int,input().split())
mod = 10**9 + 7
print((pow(2,n,mod)-1-comb(n,a)-comb(n,b))%mod)

=======
Suggestion 9

def main():
    n, a, b = map(int, input().split())
    MOD = 10**9 + 7
    if n < 2 * 10**5:
        fact = [1]
        for i in range(1, 2 * 10**5 + 1):
            fact.append((fact[-1] * i) % MOD)
        fact_inv = [pow(fact[-1], MOD - 2, MOD)]
        for i in range(2 * 10**5, 0, -1):
            fact_inv.append((fact_inv[-1] * i) % MOD)
        fact_inv.reverse()
    else:
        fact = [1]
        for i in range(1, n + 1):
            fact.append((fact[-1] * i) % MOD)
        fact_inv = [pow(fact[-1], MOD - 2, MOD)]
        for i in range(n, 0, -1):
            fact_inv.append((fact_inv[-1] * i) % MOD)
        fact_inv.reverse()
    def comb(n, r):
        return fact[n] * fact_inv[r] * fact_inv[n - r] % MOD
    print((pow(2, n, MOD) - comb(n, a) - comb(n, b) - 1) % MOD)

main()

=======
Suggestion 10

def get_input():
    return map(int, input().split())
