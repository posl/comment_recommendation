Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, y = map(int, input().split())
    if (x + y) % 3 != 0:
        print(0)
        return
    n = (x + y) // 3
    if x < n or y < n:
        print(0)
        return
    print(comb(n + x - n, x - n))

=======
Suggestion 2

def main():
    X, Y = map(int, input().split())
    if (X + Y) % 3 != 0:
        print(0)
        return
    n = (X + Y) // 3
    if not (0 <= X <= n and 0 <= Y <= n):
        print(0)
        return
    MOD = 10 ** 9 + 7
    fac = [1] * (n + 1)
    finv = [1] * (n + 1)
    for i in range(1, n + 1):
        fac[i] = fac[i - 1] * i % MOD
        finv[i] = finv[i - 1] * pow(i, MOD - 2, MOD) % MOD
    comb = lambda n, r: fac[n] * finv[r] * finv[n - r] % MOD
    print(comb(n, X))

=======
Suggestion 3

def main():
    X, Y = map(int, input().split())
    if (X + Y) % 3 != 0:
        print(0)
        return
    n = (X + Y) // 3
    if X - n < 0 or Y - n < 0:
        print(0)
        return
    X -= n
    Y -= n
    mod = 10**9 + 7
    fac = [1]
    for i in range(1, n + 1):
        fac.append(fac[-1] * i % mod)
    finv = [pow(fac[-1], mod - 2, mod)]
    for i in range(n, 0, -1):
        finv.append(finv[-1] * i % mod)
    finv.reverse()
    def comb(n, r):
        if n < r:
            return 0
        return fac[n] * finv[r] * finv[n - r] % mod
    print(comb(X + Y, X))

=======
Suggestion 4

def main():
    X, Y = map(int, input().split())
    if X < Y:
        X, Y = Y, X
    if (X + Y) % 3 != 0:
        print(0)
        return
    N = (X + Y) // 3
    M = X - N
    ans = 1
    for i in range(M):
        ans *= (N + i + 1)
        ans //= (i + 1)
        ans %= 10**9 + 7
    print(ans)

=======
Suggestion 5

def main():
    X, Y = map(int, input().split())
    if (X + Y) % 3 != 0:
        print(0)
    else:
        N = (X + Y) // 3
        if X > N or Y > N:
            print(0)
        else:
            n = N - X
            r = min(X, Y) - n
            print(combination(n + r, r))

=======
Suggestion 6

def main():
    X, Y = map(int, input().split())

    if (X + Y) % 3 != 0:
        print(0)
        return

    N = (X + Y) // 3
    if X > N or Y > N:
        print(0)
        return

    print(comb(N, X))

=======
Suggestion 7

def main():
    X, Y = map(int, input().split())
    if (X + Y) % 3 != 0:
        print(0)
        return

    N = (X + Y) // 3
    if X > N or Y > N:
        print(0)
        return

    MOD = 10 ** 9 + 7
    fact = [1] * (N + 1)
    factinv = [1] * (N + 1)
    for i in range(1, N + 1):
        fact[i] = fact[i - 1] * i % MOD
        factinv[i] = pow(fact[i], MOD - 2, MOD)

    ans = fact[N] * factinv[X] * factinv[Y] % MOD
    print(ans)

=======
Suggestion 8

def main():
    X, Y = map(int, input().split())
    if (X + Y) % 3 != 0:
        print(0)
        return

    N = (X + Y) // 3
    X -= N
    Y -= N

    if X < 0 or Y < 0:
        print(0)
        return

    MOD = 10 ** 9 + 7
    fact = [1, 1]
    fact_inv = [1, 1]
    inv = [0, 1]

    def cmb(n, r):
        if (r < 0) or (n < r):
            return 0
        r = min(r, n - r)
        return fact[n] * (fact_inv[r] * fact_inv[n - r] % MOD) % MOD

    for i in range(2, N + 1):
        fact.append((fact[-1] * i) % MOD)
        inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
        fact_inv.append((fact_inv[-1] * inv[-1]) % MOD)

    print(cmb(N, X))

=======
Suggestion 9

def main():
    x,y = map(int,input().split())
    if (x+y)%3 != 0:
        print(0)
        return
    n = (x+y)//3
    if x < n or y < n:
        print(0)
        return
    x -= n
    y -= n
    m = 10**9 + 7
    def comb(n,r):
        if n == r or r == 0:
            return 1
        if r > n-r:
            r = n-r
        numerator = 1
        denominator = 1
        for i in range(r):
            numerator *= (n-i)
            denominator *= (i+1)
            numerator %= m
            denominator %= m
        return (numerator*pow(denominator,m-2,m))%m
    print(comb(x+y,x))

=======
Suggestion 10

def main():
    X, Y = map(int, input().split())
    MOD = 10**9 + 7

    ans = 0
    if (X + Y) % 3 != 0:
        print(0)
        return

    N = (X + Y) // 3
    if N < max(X, Y):
        print(0)
        return

    ans = comb(N, X, MOD)
    print(ans)
