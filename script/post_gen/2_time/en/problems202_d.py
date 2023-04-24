Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

=======
Suggestion 2

def ncr(n,r):
    p = 1
    k = 1
    if n - r < r:
        r = n - r
    if r != 0:
        while r:
            p *= n
            k *= r
            m = gcd(p, k)
            p //= m
            k //= m
            n -= 1
            r -= 1
    else:
        p = 1
    return p

=======
Suggestion 3

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

=======
Suggestion 4

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

=======
Suggestion 5

def solve():
    a, b, k = map(int, input().split())
    comb = [[1] * (a + b + 1) for _ in range(a + b + 1)]
    for i in range(1, a + b + 1):
        for j in range(1, i):
            comb[i][j] = comb[i - 1][j - 1] + comb[i - 1][j]
    ans = []
    while a + b > 0:
        if a > 0:
            if k <= comb[a + b - 1][a - 1]:
                ans.append('a')
                a -= 1
            else:
                ans.append('b')
                b -= 1
                k -= comb[a + b][a]
        else:
            ans.append('b')
            b -= 1
    print(''.join(ans))
solve()

=======
Suggestion 6

def nCr(n,r):
    if n<r:
        return 0
    elif n==r:
        return 1
    else:
        return nCr(n-1,r-1) + nCr(n-1,r)

=======
Suggestion 7

def main():
    A, B, K = map(int, input().split())
    s = A + B
    ans = ''
    for i in range(s):
        if A == 0:
            ans += 'b'
            B -= 1
        elif B == 0:
            ans += 'a'
            A -= 1
        elif K <= comb(A + B - 1, B):
            ans += 'a'
            A -= 1
        else:
            ans += 'b'
            K -= comb(A + B - 1, B)
            B -= 1
    print(ans)

=======
Suggestion 8

def main():
    a, b, k = map(int, input().split())

    def comb(n, r):
        if n < r:
            return 0
        else:
            r = min(r, n-r)
            return fact[n] * factinv[r] * factinv[n-r] % mod

    mod = 10**9 + 7
    n = a + b
    fact = [1, 1]
    factinv = [1, 1]
    inv = [0, 1]

    for i in range(2, n+1):
        fact.append((fact[-1] * i) % mod)
        inv.append((-inv[mod%i] * (mod//i)) % mod)
        factinv.append((factinv[-1] * inv[-1]) % mod)

    ans = []
    while a + b > 0:
        if a == 0:
            ans.append('b')
            b -= 1
            continue
        elif b == 0:
            ans.append('a')
            a -= 1
            continue
        num = comb(a+b-1, a-1)
        if k <= num:
            ans.append('a')
            a -= 1
        else:
            ans.append('b')
            b -= 1
            k -= num
    print(''.join(ans))

=======
Suggestion 9

def count(n):
    if n == 0:
        return 1
    return n * count(n-1)
