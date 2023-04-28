Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X, Y = map(int, input().split())
    if (X + Y) % 3 != 0:
        print(0)
        return
    N = (X + Y) // 3
    if X > N or Y > N:
        print(0)
        return
    N -= 1
    X -= 1
    Y -= 1
    print(comb(N, X, 10**9 + 7))

=======
Suggestion 2

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
    fac = [1, 1]
    finv = [1, 1]
    inv = [0, 1]

    def COMinit():
        for i in range(2, N + 1):
            fac.append((fac[i - 1] * i) % MOD)
            inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
            finv.append((finv[i - 1] * inv[i]) % MOD)

    def COM(n, k):
        if n < k:
            return 0
        if n < 0 or k < 0:
            return 0
        return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD

    COMinit()
    print(COM(N, X))

=======
Suggestion 3

def main():
    X, Y = map(int, input().split())
    if (X + Y) % 3 != 0:
        print(0)
        return
    N = (X + Y) // 3
    if X > N or Y > N:
        print(0)
        return
    MOD = 10**9 + 7
    fact = [0] * (N + 1)
    fact[0] = 1
    for i in range(1, N + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv = [0] * (N + 1)
    inv[N] = pow(fact[N], MOD - 2, MOD)
    for i in range(N - 1, -1, -1):
        inv[i] = inv[i + 1] * (i + 1) % MOD
    print(fact[2 * N] * inv[N] * inv[N] % MOD)

=======
Suggestion 4

def main():
    X, Y = map(int, input().split())
    if (X + Y) % 3 != 0:
        print(0)
        return
    N = (X + Y) // 3
    if X > N or Y > N:
        print(0)
        return
    mod = 10**9 + 7
    X, Y = N - X, N - Y
    ans = 1
    for i in range(1, X + Y + 1):
        ans *= i
        ans %= mod
    for i in range(1, X + 1):
        ans *= pow(i, mod - 2, mod)
        ans %= mod
    for i in range(1, Y + 1):
        ans *= pow(i, mod - 2, mod)
        ans %= mod
    print(ans)

=======
Suggestion 5

def main():
    X, Y = map(int, input().split())
    if (X + Y) % 3 != 0:
        print(0)
        return
    N = (X + Y) // 3
    if X < N or Y < N:
        print(0)
        return
    print(comb(N, X - N, 10 ** 9 + 7))

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
    mod = 10 ** 9 + 7
    fact = [1] * (N + 1)
    for i in range(1, N + 1):
        fact[i] = fact[i - 1] * i % mod
    inv = [1] * (N + 1)
    inv[N] = pow(fact[N], mod - 2, mod)
    for i in range(N, 0, -1):
        inv[i - 1] = inv[i] * i % mod
    print(fact[N] * inv[X] % mod * inv[Y] % mod)

=======
Suggestion 7

def main():
    x, y = map(int, input().split())
    if (x + y) % 3 != 0:
        print(0)
    else:
        n = (x + y) // 3
        if x < n or y < n:
            print(0)
        else:
            print(comb(x, y, n))

=======
Suggestion 8

def main():
    x, y = map(int, input().split())
    if (x + y) % 3 != 0 or x < y:
        print(0)
        return
    n = (x + y) // 3
    k = x - n
    print(comb(n, k))

=======
Suggestion 9

def main():
    x,y = map(int,input().split())
    if (x+y)%3 != 0:
        print(0)
        return
    n = (x+y)//3
    if max(x,y) > n:
        print(0)
        return
    print(comb(n,x))

=======
Suggestion 10

def main():
    #input
    X, Y = map(int,input().split())
    #solve
    if (X+Y)%3!=0:
        print(0)
        return
    a = (X+Y)//3
    b = Y-a
    if a<0 or b<0:
        print(0)
        return
    mod = 10**9+7
    ans = 1
    for i in range(a):
        ans = ans*(a+b-i)*pow(i+1,mod-2,mod)%mod
    print(ans)
