Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    X, Y = map(int, input().split())
    if (X + Y) % 3 != 0:
        print(0)
        return
    N = (X + Y) // 3
    if N < max(X, Y):
        print(0)
        return
    MOD = 10**9 + 7
    fact = [1]
    for i in range(1, N + 1):
        fact.append((fact[-1] * i) % MOD)
    inv = [pow(fact[-1], MOD - 2, MOD)]
    for i in range(N, 0, -1):
        inv.append((inv[-1] * i) % MOD)
    inv.reverse()
    print((fact[N] * inv[X] * inv[Y]) % MOD)

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
    print(comb(N, X, 10**9 + 7))

=======
Suggestion 3

def main():
    X, Y = map(int, input().split())
    if (X + Y) % 3 != 0:
        print(0)
        return
    n = (X + Y) // 3
    if X > n or Y > n:
        print(0)
        return
    print(comb(n, X, 10**9 + 7))

=======
Suggestion 4

def main():
    X, Y = map(int, input().split())
    if (X + Y) % 3 != 0:
        print(0)
        return
    n = (X + Y) // 3
    if X < n or Y < n:
        print(0)
        return
    print(comb(n, X - n))

=======
Suggestion 5

def main():
    MOD = 10**9 + 7
    X, Y = map(int, input().split())
    if (X + Y) % 3 != 0:
        print(0)
        return
    n = (X + Y) // 3
    x = X - n
    y = Y - n
    if x < 0 or y < 0:
        print(0)
        return
    print(comb(n, x, MOD))

=======
Suggestion 6

def main():
    X, Y = map(int, input().split())
    if (X + Y) % 3 != 0:
        print(0)
        return
    X, Y = (X + Y) // 3, (Y - X) // 3
    if X < 0 or Y < 0:
        print(0)
        return
    print(comb(X + Y, X, 10**9 + 7))

=======
Suggestion 7

def main():
    X, Y = map(int, input().split())
    mod = 10**9+7
    if (X+Y)%3:
        print(0)
        return
    N = (X+Y)//3
    if X < Y:
        X, Y = Y, X
    if X > 2*N or Y > 2*N:
        print(0)
        return
    if X == 2*N:
        print(1)
        return
    if X == 2*N-1:
        print(N-Y+1)
        return
    if Y == 2*N:
        print(N-X+1)
        return
    if Y == 2*N-1:
        print(N-X+1)
        return
    fac = [1]*(N+1)
    for i in range(1, N+1):
        fac[i] = fac[i-1]*i%mod
    inv = [1]*(N+1)
    inv[N] = pow(fac[N], mod-2, mod)
    for i in range(N, 0, -1):
        inv[i-1] = inv[i]*i%mod
    def comb(n, r):
        if n < r:
            return 0
        return fac[n]*inv[r]*inv[n-r]%mod
    ans = 0
    for i in range(X-2*N+1):
        ans += comb(2*N-i, X-2*N-i)*comb(i, Y-2*N+i)
        ans %= mod
    print(ans)

=======
Suggestion 8

def main():
    # Read input
    X, Y = map(int, input().split())

    # Check if (X, Y) is reachable from (0, 0)
    if (X + Y) % 3 != 0:
        print(0)
        return

    # Calculate n and m
    n = (X + Y) // 3
    m = X - n

    # Check if (X, Y) is reachable from (0, 0)
    if m < 0 or m > n:
        print(0)
        return

    # Calculate the number of ways
    print(combination(n, m))

=======
Suggestion 9

def main():
    x, y = map(int, input().split())
    if (x+y) % 3 != 0 or x+y < 3:
        print(0)
        exit()

    n = (x+y)//3
    a = min(x, y) - n + 1
    b = n - max(x, y) + 1
    print(comb(n, a) % (10**9+7))
