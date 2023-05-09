Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X, Y = map(int, input().split())
    mod = 10 ** 9 + 7

    if (X + Y) % 3 != 0:
        print(0)
        return

    n = (X + Y) // 3
    m = (2 * X - Y) // 3

    if n < 0 or m < 0:
        print(0)
        return

    def comb(n, r, mod):
        if r == 0:
            return 1
        if n < r:
            return 0
        return fact[n] * fact_inv[r] * fact_inv[n-r] % mod

    fact = [1, 1]
    fact_inv = [1, 1]
    inv = [0, 1]

    for i in range(2, n + m + 1):
        fact.append((fact[-1] * i) % mod)
        inv.append((-inv[mod % i] * (mod // i)) % mod)
        fact_inv.append((fact_inv[-1] * inv[-1]) % mod)

    print(comb(n + m, n, mod))

=======
Suggestion 2

def solve(x, y):
    if (x + y) % 3 != 0:
        return 0
    n = (x + y) // 3
    m = x - n
    if m < 0 or n < 0:
        return 0
    if 2 * m < n:
        return 0
    return comb(n, m)

=======
Suggestion 3

def main():
    x, y = map(int, input().split())
    mod = 10**9 + 7
    if (x + y) % 3 != 0:
        print(0)
        return
    else:
        n = (2 * y - x) // 3
        m = (2 * x - y) // 3
        if n < 0 or m < 0:
            print(0)
            return
        else:
            ans = 1
            for i in range(1, n + 1):
                ans = ans * (m + i) * pow(i, mod - 2, mod) % mod
            print(ans)

main()

=======
Suggestion 4

def ways(x, y):
    if x + y == 0:
        return 1
    elif x < 0 or y < 0:
        return 0
    else:
        return ways(x-1, y-2) + ways(x-2, y-1)

x, y = map(int, input().split())
print(ways(x, y) % (10**9 + 7))

=======
Suggestion 5

def main():
    x, y = map(int, input().split())
    mod = 10**9 + 7
    if (x + y) % 3 != 0:
        print(0)
        return
    if (2 * x - y) % 3 != 0:
        print(0)
        return
    if (2 * y - x) % 3 != 0:
        print(0)
        return
    a = (2 * y - x) // 3
    b = (2 * x - y) // 3
    if a < 0 or b < 0:
        print(0)
        return
    n = a + b
    r = min(a, b)
    ans = 1
    for i in range(r):
        ans *= n - i
        ans %= mod
        ans *= pow(i + 1, mod - 2, mod)
        ans %= mod
    print(ans)

=======
Suggestion 6

def solve():
    X, Y = map(int, input().split())
    mod = 10**9 + 7
    if (X + Y) % 3 != 0:
        return 0
    if (2 * X - Y) % 3 != 0:
        return 0
    if (2 * Y - X) % 3 != 0:
        return 0
    a = (2 * X - Y) // 3
    b = (2 * Y - X) // 3
    if a < 0 or b < 0:
        return 0
    n = a + b
    r = a
    ans = 1
    for i in range(r):
        ans = (ans * (n - i)) % mod
        ans = (ans * pow(i + 1, mod - 2, mod)) % mod
    return ans

=======
Suggestion 7

def main():
    x,y = map(int,input().split())
    if (x+y)%3 != 0:
        print(0)
        return
    if x>y:
        x,y = y,x
    if x*2 < y:
        print(0)
        return
    if x==y:
        print(2)
        return
    print(1)
    return

=======
Suggestion 8

def knight(x,y):
    if x == 1 and y == 1:
        return 0
    elif x == 1 or y == 1:
        return 1
    else:
        return 2

x,y = map(int, input().split())
print(knight(x,y))

=======
Suggestion 9

def main():
    x, y = map(int, input().split())
    mod = 10**9 + 7
    N = 10**6 + 1
    fac = [0] * N
    fac[0] = 1
    for i in range(1, N):
        fac[i] = fac[i-1] * i % mod
    inv = [0] * N
    inv[-1] = pow(fac[-1], mod-2, mod)
    for i in range(N-2, -1, -1):
        inv[i] = inv[i+1] * (i+1) % mod
    def comb(n, r):
        if n < r:
            return 0
        return fac[n] * inv[n-r] * inv[r] % mod
    if (x+y) % 3 != 0:
        print(0)
        return
    n = (x+y)//3
    r = x - n
    if r < 0 or r > n:
        print(0)
        return
    print(comb(n, r))

=======
Suggestion 10

def count_ways(X, Y):
    # Write your code here.
    # Return the number of ways.
    return 0
