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
    mod = 10 ** 9 + 7
    fact = [1] * (N + 1)
    for i in range(1, N + 1):
        fact[i] = (fact[i - 1] * i) % mod
    fact_inv = [1] * (N + 1)
    fact_inv[N] = pow(fact[N], mod - 2, mod)
    for i in reversed(range(N)):
        fact_inv[i] = (fact_inv[i + 1] * (i + 1)) % mod
    comb = lambda n, r: (fact[n] * fact_inv[r] * fact_inv[n - r]) % mod
    print(comb(N, X))

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
    mod = 10**9 + 7
    print(comb(N, X, mod))

=======
Suggestion 3

def main():
    x, y = map(int, input().split())
    if (x + y) % 3 != 0:
        print(0)
        return
    n = (x + y) // 3
    if x < n or y < n:
        print(0)
        return
    print(comb(n, x - n))

=======
Suggestion 4

def solve():
    X, Y = map(int, input().split())
    if (X + Y) % 3 != 0:
        print(0)
        return
    N = (X + Y) // 3
    if X > N or Y > N:
        print(0)
        return
    MOD = 10**9 + 7
    fac = [1] * (N + 1)
    for i in range(1, N + 1):
        fac[i] = fac[i - 1] * i % MOD
    ifac = [1] * (N + 1)
    ifac[N] = pow(fac[N], MOD - 2, MOD)
    for i in range(N - 1, -1, -1):
        ifac[i] = ifac[i + 1] * (i + 1) % MOD
    def comb(n, k):
        return fac[n] * ifac[k] % MOD * ifac[n - k] % MOD
    print(comb(N, X))
    return

=======
Suggestion 5

def main():
    X, Y = map(int, input().split())
    MOD = 10**9 + 7

    if (X + Y) % 3 != 0:
        print(0)
        return

    n = (X + Y) // 3
    if X < n or Y < n:
        print(0)
        return

    x = X - n
    y = Y - n

    print(comb(n, x, MOD))

=======
Suggestion 6

def main():
    X, Y = map(int, input().split())
    if X % 2 != Y % 2:
        print(0)
        return
    if X == 0 and Y == 0:
        print(1)
        return
    if X == 0 or Y == 0:
        print(0)
        return
    if X == 1 and Y == 1:
        print(2)
        return
    if X == 1 or Y == 1:
        print(0)
        return
    if X == 2 and Y == 2:
        print(2)
        return
    if X == 2 or Y == 2:
        print(0)
        return
    if X == 3 and Y == 3:
        print(2)
        return
    if X == 3 or Y == 3:
        print(0)
        return
    if X == 4 and Y == 4:
        print(4)
        return
    if X == 4 or Y == 4:
        print(0)
        return
    if X == 5 and Y == 5:
        print(4)
        return
    if X == 5 or Y == 5:
        print(0)
        return
    if X == 6 and Y == 6:
        print(8)
        return
    if X == 6 or Y == 6:
        print(0)
        return
    if X == 7 and Y == 7:
        print(8)
        return
    if X == 7 or Y == 7:
        print(0)
        return
    if X == 8 and Y == 8:
        print(16)
        return
    if X == 8 or Y == 8:
        print(0)
        return
    if X == 9 and Y == 9:
        print(16)
        return
    if X == 9 or Y == 9:
        print(0)
        return
    if X == 10 and Y == 10:
        print(32)
        return
    if X == 10 or Y == 10:
        print(0)
        return
    if X == 11 and Y == 11:
        print(32)
        return
    if X == 11

=======
Suggestion 7

def main():
    X, Y = map(int, input().split())
    if X % 2 != Y % 2:
        print(0)
        exit()
    if X == Y == 0:
        print(1)
        exit()
    if X == Y:
        print(2)
        exit()
    print(0)

main()

=======
Suggestion 8

def main():
    x, y = map(int, input().split())
    if (x + y) % 3 != 0:
        print(0)
        return
    x, y = sorted([x, y])
    n = (x + y) // 3
    m = min(x, y) - n
    ans = 1
    for i in range(n + 1, n + m + 1):
        ans = ans * i % (10**9 + 7)
    for i in range(1, m + 1):
        ans = ans * pow(i, -1, 10**9 + 7) % (10**9 + 7)
    print(ans)

=======
Suggestion 9

def main():
    X, Y = map(int, input().split())
    if X % 2 != Y % 2:
        print(0)
        return
    X, Y = (X + Y) // 2, (X - Y) // 2
    if X < 0 or Y < 0:
        print(0)
        return
    MOD = 10 ** 9 + 7
    dp = [0] * (X + 1)
    dp[0] = 1
    for i in range(Y + 1):
        for j in range(X, i - 1, -1):
            dp[j] = (dp[j] + dp[j - 1]) % MOD
    print(dp[X])

=======
Suggestion 10

def main():
    X,Y = map(int,input().split())
    if (X+Y) % 3 != 0:
        print(0)
        return
    n = (X+Y)//3
    if X > n or Y > n:
        print(0)
        return
    mod = 10**9+7
    ans = 1
    for i in range(n+1,n+X+1):
        ans *= i
        ans %= mod
    for i in range(1,X+1):
        ans *= pow(i,mod-2,mod)
        ans %= mod
    print(ans)
